#!/usr/bin/env python3
"""Filtered logger, use regex to escape/ hide user data fields"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message using regex."""
    regex = fr"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(regex, lambda x: f"{x.group(1)}={redaction}", message)
