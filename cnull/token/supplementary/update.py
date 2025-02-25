import os
from datetime import datetime
from ..json_handler import JsonHandler

class TokenUpdater:
    def __init__(self):
        self.tokens_file = 'cnullapi.json'
        self.json_handler = JsonHandler(self.tokens_file)

    def update_token_last_used(self, user_id, token):
        data = self.json_handler.load_json()
        
        if str(user_id) not in data:
            return False
            
        user_data = data[str(user_id)]
        for token_data in user_data['tokens']:
            if token_data['value'] == token:
                token_data['last_used'] = datetime.now().isoformat()
                self.json_handler.save_json(data)
                return True
        return False

    def remove_expired_tokens(self):
        data = self.json_handler.load_json()
        current_time = datetime.now()
        
        for user_id in data:
            user_data = data[user_id]
            valid_tokens = []
            
            for token_data in user_data['tokens']:
                if token_data['expires']:
                    expiration = datetime.fromisoformat(token_data['expires'])
                    if expiration > current_time:
                        valid_tokens.append(token_data)
                else:
                    valid_tokens.append(token_data)
                    
            user_data['tokens'] = valid_tokens
            
        self.json_handler.save_json(data)

    def update_token_permissions(self, user_id, token, new_permissions):
        data = self.json_handler.load_json()
        
        if str(user_id) not in data:
            return False
            
        user_data = data[str(user_id)]
        for token_data in user_data['tokens']:
            if token_data['value'] == token:
                token_data['permissions'] = new_permissions
                self.json_handler.save_json(data)
                return True
        return False

    def update_token_expiration(self, user_id, token, new_expiration):
        data = self.json_handler.load_json()
        
        if str(user_id) not in data:
            return False
            
        user_data = data[str(user_id)]
        for token_data in user_data['tokens']:
            if token_data['value'] == token:
                token_data['expires'] = new_expiration.isoformat() if new_expiration else None
                self.json_handler.save_json(data)
                return True
        return False
