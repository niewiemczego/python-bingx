import hashlib
import hmac
import os

import pytest
from dotenv import load_dotenv

from bingx._helpers import generate_hash, generate_timestamp

load_dotenv()


@pytest.fixture
def secret_key() -> str:
    return os.getenv("SECRET_KEY")


def test_generate_timestamp():
    timestamp = generate_timestamp()
    assert isinstance(timestamp, int)
    assert timestamp > 0


def test_generate_hash(secret_key: str):
    query_string = "example_query_string"
    expected_hash = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256)
    result_hash = generate_hash(secret_key, query_string)

    assert isinstance(result_hash, hmac.HMAC)
    assert result_hash.digest() == expected_hash.digest()
    assert result_hash.hexdigest() == expected_hash.hexdigest()