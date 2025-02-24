import uuid
# token_creator.py
class TokenCreator:
    def generate_token(self):
        return str(uuid.uuid4())