#!/usr/bin/env python3
"""Session with expiration date"""
from api.v1.auth.session_auth import SessionAuth
from uuid import uuid4
from models.user import User
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    def __init__(self):
        """INIT a new instance of session w expiry"""
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a session"""
        session_id = super().create_session(user_id)
        if not session_id or type(session_id) is not str:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """gets used_id for session_id"""
        if not session_id:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id.get(session_id).get('user_id')
        try:
            is_created = self.user_id_by_session_id.get(session_id).get('created_at')  # noqa
        except Exception:
            return None
        duration_obj = timedelta(seconds=self.session_duration)
        if is_created + duration_obj < datetime.now():
            return None
        return self.user_id_by_session_id.get(session_id).get('user_id')
