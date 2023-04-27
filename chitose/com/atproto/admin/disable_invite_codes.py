from __future__ import annotations
import chitose
import typing

def disable_invite_codes(service: str, headers: dict[str, str], codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None):
    """Disable some set of codes and/or all codes associated with a set of users"""
    return chitose.xrpc.call('com.atproto.admin.disableInviteCodes', [], {'codes': codes, 'accounts': accounts}, service, {'Content-Type': 'application/json'} | headers)