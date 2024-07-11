#!/usr/bin/env python3
"""Session authentication mechanism"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session authentication class
    that inherits from Auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session based on the authenticated user"""
        if not user_id or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieve user_id based on session_id"""
        if not session_id or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)