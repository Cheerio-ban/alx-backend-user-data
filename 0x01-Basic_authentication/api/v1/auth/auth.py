#!/usr/bin/env python3

""" Authentication Base Module. """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication Base Class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth """
        if not path:
            return True
        if not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        for paths in excluded_paths:
            if paths[:-1] == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header. """
        if not request:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user in session """
        return None
