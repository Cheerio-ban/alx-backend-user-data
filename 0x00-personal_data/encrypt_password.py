#!/usr/bin/env python3

""" Using Bcryption in python """

import bcrypt


def hash_password(strings: str) -> bytes:
    """Hashes a password using bcrypt"""
    return bcrypt.hashpw(strings.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password hash"""
    return bcrypt.checkpw(password.encode(), hashed_password)
