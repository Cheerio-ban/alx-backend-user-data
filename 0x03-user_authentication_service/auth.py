#!/usr/bin/env python3

"""Auth Module."""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes Password passed to it."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
