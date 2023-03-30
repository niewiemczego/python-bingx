import hashlib
import hmac
import time
from dataclasses import asdict
from enum import Enum
from typing import Any


class DictMixin:
    def to_dict(self) -> dict[str, Any]:
        def convert_value(value):
            if isinstance(value, Enum):
                return value.value
            return value
        return {k: convert_value(v) for k, v in asdict(self).items() if v is not None}


def generate_timestamp() -> int:
    """
    It returns the current time in milliseconds
    """
    return int(time.time() * 10 ** 3)


def generate_hash(key: str, query_string: str) -> hmac.HMAC:
    """
    It returns the hash of the query string using the secret key with the SHA256 algorithm

    :param key: The secret key that you'll use to generate the hash
    :param query_string: The query string that you want to sign
    """
    return hmac.new(key.encode(), query_string.encode(), hashlib.sha256)
