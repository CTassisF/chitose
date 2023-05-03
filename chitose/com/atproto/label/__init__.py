# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .query_labels import _query_labels
from .defs import *
from .query_labels import *
from .subscribe_labels import *

class Label:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def query_labels(self, uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """Find labels relevant to the provided URI patterns.


        :param uri_patterns: List of AT URI patterns to match (boolean 'OR'). Each may be a prefix (ending with '*'; will match inclusive of the string leading to '*'), or a full URI

        :param sources: Optional list of label sources (DIDs) to filter on
        """
        return _query_labels(self.service, self.headers, uri_patterns, sources, limit, cursor)