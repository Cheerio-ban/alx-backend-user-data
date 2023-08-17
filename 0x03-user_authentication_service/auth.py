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
        user = self._db.find_user_by(email=email)
        except NoResultFound:
            passw = _hash_password(password).decode('utf-8')
            new_user = self._db.add_user(email, passw)
            return new_user
        raise ValueError("User {} already exists".format(email))
