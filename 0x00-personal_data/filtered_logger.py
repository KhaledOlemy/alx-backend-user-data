#!/usr/bin/env python3
"""Filtered logger, use regex to escape/ hide user data fields"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates specified fields in a log message."""
    pattern = '|'.join(f'(?<={field}=)[^{separator}]+' for field in fields)
    return re.sub(pattern, redaction, message)
