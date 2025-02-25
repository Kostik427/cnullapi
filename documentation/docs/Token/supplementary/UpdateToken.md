
# UpdateToken Documentation

The `TokenUpdater` class provides functionality for managing and updating API tokens stored in a JSON file.

## Class Overview

### TokenUpdater

Main class for handling token updates and management.

#### Constructor

def __init__(self):
    self.tokens_file = 'cnullapi.json'
    self.json_handler = JsonHandler(self.tokens_file)


#### Methods

##### update_token_last_used(user_id, token)
Updates the last used timestamp for a specific token.
- Parameters:
  - user_id: User identifier
  - token: Token value to update
- Returns: Boolean indicating success

##### remove_expired_tokens()
Removes all expired tokens from the storage.
- No parameters
- No return value

##### update_token_permissions(user_id, token, new_permissions)
Updates permissions for a specific token.
- Parameters:
  - user_id: User identifier
  - token: Token value to update
  - new_permissions: New permissions to set
- Returns: Boolean indicating success

##### update_token_expiration(user_id, token, new_expiration)
Updates expiration date for a specific token.
- Parameters:
  - user_id: User identifier
  - token: Token value to update
  - new_expiration: New datetime for expiration
- Returns: Boolean indicating success

## Usage Example


updater = TokenUpdater()

# Update token's last used timestamp
updater.update_token_last_used("user123", "token_value")

# Remove expired tokens
updater.remove_expired_tokens()

# Update token permissions
new_permissions = ["read", "write"]
updater.update_token_permissions("user123", "token_value", new_permissions)

# Update token expiration
from datetime import datetime, timedelta
new_expiration = datetime.now() + timedelta(days=30)
updater.update_token_expiration("user123", "token_value", new_expiration)


## Data Structure

The tokens are stored in JSON format with the following structure:

{
    "user_id": {
        "tokens": [
            {
                "value": "token_string",
                "last_used": "ISO-format-datetime",
                "expires": "ISO-format-datetime",
                "permissions": ["permission1", "permission2"]
            }
        ]
    }
}

