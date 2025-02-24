import json


# json_handler.py
class JsonHandler:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_json(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    def save_json(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)