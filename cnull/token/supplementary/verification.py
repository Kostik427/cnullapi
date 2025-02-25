from ..json_handler import JsonHandler

class VerifyToken:
    def __init__(self, tokens_file='cnullapi.json'):
        self.tokens_file = tokens_file
        self.json_handler = JsonHandler(self.tokens_file)

    def verify_token(self, user_id, token):
        data = self.json_handler.load_json()

        if str(user_id) not in data:
            return False

        user_data = data[str(user_id)]
        for token_data in user_data['tokens']:
            if token_data['value'] == token:
                return True
        return False
