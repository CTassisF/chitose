# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_profile(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Get detailed profile view of an actor."""
    return call('app.bsky.actor.getProfile', [('actor', actor)], None, {})