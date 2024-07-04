#!/usr/bin/env python3
"""Encrypting passwords, hasing to be stored in db"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password, password):
    """Validate that the provided password matches the hashed password."""
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
