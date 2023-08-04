#!/usr/bin/env python3

""" Using Bcrypt. """

import bcrypt


def hash_password(string: str):
    """Hashes a password using bcrypt"""
    salt = bcrypt.gensalt()
    byter = string.encode('utf-8')
    pwd_hash = bcrypt.hashpw(byter, salt)
    return pwd_hash
