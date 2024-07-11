#!/usr/bin/env python3
"""
Base model for Authorization
using headers (the basic one)
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class, this will be the base class for
    the upcoming authorization systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication for path
        """
        if not path or not excluded_paths:
            return True
        temp_path = path if path.endswith('/') else "{}/".format(path)
        if temp_path in excluded_paths:
            return False
        if [p for p in excluded_paths if path.startswith(p.replace('*', ''))]:
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

    def session_cookie(self, request=None):
        """get _my_session_id cookie value"""
        if not request:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
