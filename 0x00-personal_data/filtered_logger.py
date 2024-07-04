#!/usr/bin/env python3
"""Filtered logger, use regex to escape/ hide user data fields"""
import re
from typing import List
import logging
import mysql.connector
import os


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
        """INIT method to declare fields"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format text to escape fields"""
        text = super().format(record)
        return filter_datum(self.fields, self.REDACTION, text, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Create a logger for a csv file `user data`"""
    logger = logging.getLogger("user_data")
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(streamHandler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Creates a connectino to a remote database """
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pswd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    conn = mysql.connector.connect(
        user=db_user,
        password=db_pswd,
        host=db_host,
        database=db_name,
        port=3306
    )
    return conn
