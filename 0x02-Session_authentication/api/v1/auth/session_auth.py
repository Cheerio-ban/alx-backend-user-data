#!/usr/bin/env python3

"""
Module of SessionAuth Object
"""

from api.v1.auth.auth import Auth
from os import setenv
import uuid
from typing import Dict, Any, Union


class SessionAuth(Auth):
    """Session Auth base class. """
    user_id_by_session_id: Dict[str, Any] = {}

    def create_session(self, user_id: str = None) -> Union[str, None]:
        """Creates a session."""
        if not user_id:
            return
        if not isinstance(user_id, str):
            return
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets a particular user id based on session id"""
        if not session_id:
            return
        if not isinstance(session_id, str):
            return
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """Returns a cookie from a request object"""
        if not request:
            return
        setenv(SESSION_NAME) = '_my_session_id'
        return request.cookie.get('_my_session_id')
