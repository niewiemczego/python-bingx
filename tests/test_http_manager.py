import os

import pytest
from dotenv import load_dotenv

from bingX._http_manager import _HTTPManager
from bingX.exceptions import ClientError, InvalidMethodException, ServerError

load_dotenv()

class TestHTTPManager:
    @pytest.fixture()
    def http_manager(self) -> _HTTPManager:
        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")
        return _HTTPManager(api_key, secret_key)

    def test_request_get_valid(self, http_manager: _HTTPManager):
        response = http_manager._request("GET", "/openApi/swap/v2/quote/contracts")
        assert isinstance(response.json(), dict)

    def test_request_get_invalid(self, http_manager: _HTTPManager):
        with pytest.raises(ClientError):
            http_manager._request("GET", "/openApi/swap/v2/quote/contracts1")

    #TODO: add test for post, put, delete

    def test_generate_signature(self, http_manager: _HTTPManager):
        query_string = "foo=bar&baz=qux"
        expected_signature = "402028be4bd6689f237c39366108c5d67422134d89b3a9b6e651a71599d8449e" # it has been generated with secret_key from .env
        assert http_manager._generate_signature(query_string) == expected_signature

    def test_generate_query_string(self, http_manager: _HTTPManager):
        payload = {"foo": "bar", "baz": "qux"}
        generated_query_string = http_manager._generate_query_string(payload)
        generated_query_string_timestamp = generated_query_string[generated_query_string.find("timestamp=") + len("timestamp="):generated_query_string.find("timestamp=") + len("timestamp=") + 13]
        signature = http_manager._generate_signature(f"foo=bar&baz=qux&timestamp={generated_query_string_timestamp}")
        expected_query_string = f"foo=bar&baz=qux&timestamp={generated_query_string_timestamp}&signature={signature}"
        assert generated_query_string == expected_query_string

    def test_invalid_method(self, http_manager: _HTTPManager):
        with pytest.raises(InvalidMethodException):
            http_manager._request("INVALID", "/openApi/swap/v2/trade/order")

    def test_server_error(self, http_manager: _HTTPManager):
        with pytest.raises(ServerError):
            http_manager._request("PUT", "/openApi/swap/v2/trade/order", payload={"test": "test"})

    def test_client_error(self, http_manager: _HTTPManager):
        with pytest.raises(ClientError):
            http_manager._request("GET", "/openApi/swap/v2/trade", payload={"test": "test"})