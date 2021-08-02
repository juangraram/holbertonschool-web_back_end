#!/usr/bin/python3
import re
from typing import List
"""Regex-ing"""


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """function called filter_datum that returns the log message"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
