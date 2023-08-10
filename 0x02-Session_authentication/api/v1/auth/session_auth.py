#!/usr/bin/env python3

"""
Module of SessionAuth Object
"""

from api.v1.auth.auth import Auth
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

    def current_user(self, request=None) -> Union[User, None]:
        """Return the current user from db using its id from the session"""
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        return User.get(user_id)
