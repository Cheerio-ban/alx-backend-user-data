#!/usr/bin/env python3

"""Auth Module."""

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes Password passed to it."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers users to the database. """
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            raise ValueError("User {} already exists".format(email))
        passw = _hash_password(password)
        new_user = self._db.add_user(email, passw)
        return new_user
