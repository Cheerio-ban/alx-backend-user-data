#!/usr/bin/env python3
""" Filtered Logger. """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces fields with a redaction using re.sub
    """
    for field in fields:
        message = re.sub(fr'{field}=[^{separator}]*',
                         f'{field}={redaction}', message)
    return message
