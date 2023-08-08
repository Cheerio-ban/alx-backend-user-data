#!/usr/bin/env python3

"""
Contains Basic auth
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth Model """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts authorization header. """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes base64 authorization header """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        return base64.b64decode(base_authorization_header).decode('utf-8')
