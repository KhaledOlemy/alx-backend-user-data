#!/usr/bin/env python3
"""
Basic Authentication class for Authorization
using headers
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    pass
