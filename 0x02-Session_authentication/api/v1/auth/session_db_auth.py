#!/usr/bin/env python3
"""Session storage model to store sessions details"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session with expiration date with db storage
    in case of a failure
    """
    def create_session(self, user_id=None):
        """INIT a new instance of session w expiry w db storage
        """
        session_id = super().create_session(user_id)
        if not session_id or type(session_id) is not str:
            return None
        init_param = {
            "user_id": user_id,
            "session_id": session_id
        }
        new_user_session = UserSession(**init_param)
        new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Creates a session and store it in db
        """
        if not session_id:
            return None
        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions:
            return None
        user_session = user_sessions[0]
        if self.session_duration <= 0:
            return self.user_session.user_id
        duration_obj = timedelta(seconds=self.session_duration)
        if user_session.created_at + duration_obj < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """destroys user session from db
        """
        if not request:
            return False
        if not self.session_cookie(request):
            return False
        session_id = self.session_cookie(request)
        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions:
            return False
        user_sessions[0].remove()
        return True
