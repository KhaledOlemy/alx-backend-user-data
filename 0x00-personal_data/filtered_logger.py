#!/usr/bin/env python3
"""Filtered logger, use regex to escape/ hide user data fields"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # noqa
    """Obfuscates specified fields in a log message using regex."""
    regex = fr"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(regex, lambda x: f"{x.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        text = super().format(record)
        return filter_datum(self.fields, self.REDACTION, text, self.SEPARATOR)
