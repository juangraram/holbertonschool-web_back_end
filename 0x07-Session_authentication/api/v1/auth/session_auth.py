#!/usr/bin/env python3
""" Session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session ID by user ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return user ID for session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """  to return the User ID based on the cookie _my_session_id
        """
        session_id_by_cookie = self.session_cookie(request)
        if session_id_by_cookie is None:
            return None
        user_id = self.user_id_for_session_id(session_id_by_cookie)
        if user_id is None:
            return None
        from models.user import User
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Delete current session
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
