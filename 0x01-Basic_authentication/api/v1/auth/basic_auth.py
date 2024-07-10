#!/usr/bin/env python3
"""
Basic Authentication class for Authorization
using headers
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa
        """Decodes the base64 authorization header
        """
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('UTF-8')  # noqa
        except binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):  # noqa
        """Extracts user credentials from the authorization header
        """
        if not decoded_base64_authorization_header:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))
