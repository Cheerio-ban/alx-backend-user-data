#!/usr/bin/env python3

"""
Module of SessionAuth Object
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Auth base class. """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session."""
        if not user_id:
            return
        if not isinstance(user_id, str):
            return
        uid = str(uuid.uuid4())
        user_id_by_session_id[uid] = user_id
        return uid
