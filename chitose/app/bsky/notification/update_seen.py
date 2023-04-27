from __future__ import annotations
import chitose

def update_seen(service: str, headers: dict[str, str], seen_at: str):
    """Notify server that the user has seen notifications."""
    return chitose.xrpc.call('app.bsky.notification.updateSeen', [], {'seenAt': seen_at}, service, {'Content-Type': 'application/json'} | headers)