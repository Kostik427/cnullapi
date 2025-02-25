# CreateToken 

The `CreateToken` class manages token creation and storage for different user types.

## Overview

The `CreateToken` class handles token generation, storage, and management with different expiration periods and permissions based on user types.

## Dependencies

- `os`: For file system operations
- `datetime`, `timedelta`: For handling token expiration times
- `JsonHandler`: Custom class for JSON file operations
- `TokenCreator`: Custom class for token generation

## Class Attributes

- `tokens_file`: Stores tokens in 'cnullapi.json'
- `token_ttl`: Token time-to-live configurations:
  - default: 7 days
  - premium: 30 days
  - op: Never expires

## Methods

### `__init__()`

Initializes the CreateToken instance with:
- JSON file handler
- Token creator
- Token TTL settings
- Creates empty JSON file if not exists

### `create_token(user_id, token_type, custom_max_tokens=None, custom_token_generator=None, permissions=None)`

Creates and stores a new token for a user.

Parameters:
- `user_id`: Unique identifier for the user
- `token_type`: Type of token (default/premium/op)
- `custom_max_tokens`: Optional custom token limits
- `custom_token_generator`: Optional custom token generation function
- `permissions`: Optional list of permissions (defaults to ['read'])

Default token limits:
- default: 5 tokens
- premium: 25 tokens
- op: Unlimited tokens

Returns:
- Token string if created successfully
- None if user has reached token limit

Token storage format:

{
    "value": "token_string",
    "expires": "expiration_datetime",
    "permissions": ["permissions_list"],
    "created_at": "creation_datetime",
    "last_used": null
}

- Default expiration time is 1 hour (3600 seconds) if not specified
