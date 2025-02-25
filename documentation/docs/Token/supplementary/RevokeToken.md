## RevokeToken Documentation

The `RevokeToken` class provides functionality to revoke user authentication tokens stored in a JSON file.

### Class Overview

from ..json_handler import JsonHandler

class RevokeToken:
    def __init__(self, tokens_file='cnullapi.json')
    def _revoke_token(self, user_id, token)


### Constructor Parameters
- `tokens_file` (str, optional): Path to the JSON file storing tokens. Defaults to 'cnullapi.json'.

### Methods

#### _revoke_token(user_id, token)
Revokes a specific token for a given user.

**Parameters:**
- `user_id` (str/int): The ID of the user whose token should be revoked
- `token` (str): The token value to revoke

**Returns:**
- `bool`: True if token was successfully revoked, False if user or token not found

**Process:**
1. Loads data from JSON file
2. Checks if user exists
3. Searches for matching token in user's tokens list
4. Removes token if found and saves updated data
5. Returns operation result

### Example Usage

revoke = RevokeToken()
success = revoke._revoke_token("123", "abc123token")
