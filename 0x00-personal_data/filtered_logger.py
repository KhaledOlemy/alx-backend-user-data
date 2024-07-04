#!/usr/bin/env python3
"""Filtered logger, use regex to escape/ hide user data fields"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates specified fields in a log message using regex."""
    regex = fr"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(regex, lambda x: f"{x.group(1)}={redaction}", message)
