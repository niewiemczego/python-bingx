import hashlib
import hmac
import time


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
