import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.spot.other import Other

load_dotenv()

class TestTrade:
    @pytest.fixture
    def other(self) -> Other:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Other(api_key, secret_key)

    def test_generate_listen_key_valid(self, other: Other):
        response = other.generate_listen_key()
        assert isinstance(response, dict)
        assert isinstance(response.get("listenKey"), str)

    def test_extend_listen_key_validity_period_valid(self, other: Other):
        response = other.generate_listen_key()
        listen_key = response.get("listenKey")
        assert isinstance(listen_key, str)
        response = other.extend_listen_key_validity_period(listen_key)
        assert response == 200

    def test_extend_listen_key_validity_period_invalid(self, other: Other):
        fake_listen_key = "a8ea75681542e66f1a50a1616dd06ed77dab61baa0c296bca03a9b13ee5f2dd7"
        response = other.extend_listen_key_validity_period(fake_listen_key)
        assert response == 404

    def test_delete_listen_key_valid(self, other: Other):
        response = other.generate_listen_key()
        listen_key = response.get("listenKey")
        response = other.delete_listen_key(listen_key)
        assert response == 200
