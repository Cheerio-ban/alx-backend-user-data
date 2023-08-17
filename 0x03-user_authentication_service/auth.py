#!/usr/bin/env python3

"""Auth Module."""

import bcrypt
from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes Password passed to it."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """Returns uuid generated string"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers users to the database. """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            passw = _hash_password(password).decode('utf-8')
            new_user = self._db.add_user(email, passw)
            return new_user
        raise ValueError("User {} already exists".format(email))
