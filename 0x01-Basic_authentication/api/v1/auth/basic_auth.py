#!/usr/bin/env python3
"""
Basic Authentication class for Authorization
using headers
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication system
    decided by env vars
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa
        """Returns only the base64 part
        """
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[-1]
