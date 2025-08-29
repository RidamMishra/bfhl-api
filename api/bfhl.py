from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            input_data = data.get('data', [])
            
            even_numbers = []
            odd_numbers = []
            alphabets = []
            special_characters = []
            numbers_sum = 0
            alpha_chars = []
            
            for item in input_data:
                item_str = str(item)
                
                if is_integer(item_str):
                    num = int(item_str)
                    numbers_sum += num
                    
                    if num % 2 == 0:
                        even_numbers.append(item_str)
                    else:
                        odd_numbers.append(item_str)
                elif item_str.isalpha():
                    alphabets.append(item_str.upper())
                    for char in item_str:
                        alpha_chars.append(char)
                else:
                    special_characters.append(item_str)
            
            concat_string = ""
            alpha_chars.reverse()
            
            for i, char in enumerate(alpha_chars):
                if i % 2 == 0:
                    concat_string += char.upper()
                else:
                    concat_string += char.lower()
            
            response = {
                "is_success": True,
                "user_id": "ridam_mishra_29082025",
                "email": "mridam518@gmail.com",
                "roll_number": "22BPS1116",
                "odd_numbers": odd_numbers,
                "even_numbers": even_numbers,
                "alphabets": alphabets,
                "special_characters": special_characters,
                "sum": str(numbers_sum),
                "concat_string": concat_string
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            error_response = {
                "is_success": False,
                "error_message": str(e)
            }
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode('utf-8'))