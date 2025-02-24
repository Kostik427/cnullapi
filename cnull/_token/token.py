import os
from datetime import datetime, timedelta
from .json_handler import JsonHandler
from .token_creator import TokenCreator



class CreateToken:
    def __init__(self):
        self.tokens_file = 'cnullapi.json'
        self.json_handler = JsonHandler(self.tokens_file)
        self.token_creator = TokenCreator()
        self.token_ttl = {
            'default': timedelta(days=7),
            'premium': timedelta(days=30),
            'op': None  # never expires
        }
    
        if not os.path.exists(self.tokens_file):
            self.json_handler.save_json({})

    def _create_token(self, user_id, token_type, custom_max_tokens=None, custom_token_generator=None, permissions=None):
        data = self.json_handler.load_json()
        token = custom_token_generator() if custom_token_generator else self.token_creator.generate_token()
    
        if str(user_id) not in data:
            data[str(user_id)] = {
                'tokens': [],
                'type': token_type
            }
    
        user_data = data[str(user_id)]
        max_tokens = custom_max_tokens or {
            'default': 5,
            'premium': 25,
            'op': float('inf')
        }
    
        if len(user_data['tokens']) >= max_tokens.get(user_data['type'], 5):
            return None
        
        expiration = None
        if self.token_ttl.get(user_data['type']):
            expiration = datetime.now() + self.token_ttl[user_data['type']]
        
        user_data['tokens'].append({
            'value': token,
            'expires': expiration.isoformat() if expiration else None,
            'permissions': permissions or ['read'],
            'created_at': datetime.now().isoformat(),
            'last_used': None
        })
        self.json_handler.save_json(data)
        return token
    
    