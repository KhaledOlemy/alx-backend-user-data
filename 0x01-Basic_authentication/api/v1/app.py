#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
excluded_paths = [
    '/api/v1/status/',
    '/api/v1/unauthorized/',
    '/api/v1/forbidden/'
]
auth = None
if os.getenv("AUTH_TYPE") == 'auth':
    auth = Auth()
elif os.getenv("AUTH_TYPE") == 'basic_auth':
    auth = BasicAuth()


@app.before_request
def handle_authorization() -> str:
    """Handle authorization before any request
    """
    if not auth:
        return
    if not auth.require_auth(excluded_paths=excluded_paths, path=request.path):
        return
    if not auth.authorization_header(request):
        abort(401)
    if not auth.current_user(request):
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_man(error) -> str:
    """Block unauthorized with a JSON"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_man(error) -> str:
    """Block forbidden requests with a JSON"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
