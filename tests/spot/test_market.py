
import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.spot.market import Market

load_dotenv()

class TestMarket:
    @pytest.fixture
    def market(self) -> Market:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Market(api_key, secret_key)

    def test_get_symbols_valid(self, market: Market):
        response = market.get_symbols()
        assert isinstance(response, dict)

    def test_get_symbols_valid_symbol(self, market: Market):
        response = market.get_symbols("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_symbols_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_symbols("BTCUSDT")

    def test_get_transaction_records_valid(self, market: Market):
        response = market.get_transaction_records("BTC-USDT")
        assert isinstance(response, list)

    def test_get_transaction_records_invalid(self, market: Market):
        with pytest.raises(ClientError):
            market.get_transaction_records("BTCUSDT")

    def test_get_depth_details_valid(self, market: Market):
        response = market.get_depth_details("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_depth_details_invalid(self, market: Market):
        with pytest.raises(ClientError):
            market.get_depth_details("BTCUSDT")