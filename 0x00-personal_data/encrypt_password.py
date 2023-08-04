#!/usr/bin/env python3

""" Using Bcryption in python """

import bcrypt


def hash_password(password: str) -> bytes:
    """Return the hash of a password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password hash"""
    return bcrypt.checkpw(password.encode(), hashed_password)
