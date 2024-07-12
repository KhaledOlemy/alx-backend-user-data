#!/usr/bin/env python3
"""User session model to store session details"""
from models.base import Base


class UserSession(Base):
    """User session class to store session details"""
    def __init__(self, *args: list, **kwargs: dict):
        """INIT user session instances"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
