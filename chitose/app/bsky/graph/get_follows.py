from __future__ import annotations
import chitose
import typing

def get_follows(service: str, headers: dict[str, str], actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
    """Who is an actor following?"""
    return chitose.xrpc.call('app.bsky.graph.getFollows', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)