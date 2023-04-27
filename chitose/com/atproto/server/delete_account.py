from __future__ import annotations
import chitose

def delete_account(service: str, headers: dict[str, str], did: str, password: str, token: str):
    """Delete a user account with a token and password."""
    return chitose.xrpc.call('com.atproto.server.deleteAccount', [], {'did': did, 'password': password, 'token': token}, service, {'Content-Type': 'application/json'} | headers)