#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def handle_login():
    """Executes the login operation"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    psswd = request.form.get('password')
    if not psswd:
        return jsonify({"error": "password missing"}), 400
    target_user = User.search({"email": email})
    if not target_user:
        return jsonify({"error": "no user found for this email"}), 404
    target_user = target_user[0]
    if not target_user.is_valid_password(psswd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(target_user.to_json()['id'])
    out_user = jsonify(target_user.to_json())
    out_user.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return out_user
