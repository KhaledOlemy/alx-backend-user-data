#!/usr/bin/env python3
"""
Base model for Authorization
using headers (the basic one)
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class, this will be the base class for
    the upcoming authorization systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication for path
        """
        if not path or not excluded_paths:
            return True
        path = path if path.endswith('/') else "{}/".format(path)
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get authorization header
        """
        if not request:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """Get current used authenticated
        """
        return None
