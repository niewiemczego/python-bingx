import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.perpetual.v2.market import Market

load_dotenv()

class TestMarket:
    @pytest.fixture
    def market(self) -> Market:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Market(api_key, secret_key)

    def test_get_contract_info(self, market: Market):
        response = market.get_contract_info()
        assert isinstance(response, list)

    def test_get_latest_price_of_trading_pair_valid(self, market: Market):
        response = market.get_latest_price_of_trading_pair()
        assert isinstance(response, list)

    def test_get_latest_price_of_trading_pair_valid_symbol(self, market: Market):
        response = market.get_latest_price_of_trading_pair("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_latest_price_of_trading_pair_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_latest_price_of_trading_pair("BTCUSDT")

    def test_get_market_depth_valid_symbol(self, market: Market):
        response = market.get_market_depth("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_market_depth_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_market_depth("BTCUSDT")

    def test_get_market_depth_invalid_limit(self, market: Market):
        with pytest.raises(ClientError):
            market.get_market_depth("BTC-USDT", 123456)

    def test_get_latest_trade_of_trading_pair_valid_symbol(self, market: Market):
        response = market.get_latest_trade_of_trading_pair("BTC-USDT")
        assert isinstance(response, list)

    def test_get_latest_trade_of_trading_pair_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_latest_trade_of_trading_pair("BTCUSDT")

    def test_get_latest_trade_of_trading_pair_invalid_limit(self, market: Market):
        with pytest.raises(ClientError):
            market.get_latest_trade_of_trading_pair("BTC-USDT", 123456)

    def test_get_current_funding_rate_valid(self, market: Market):
        response = market.get_current_funding_rate()
        assert isinstance(response, list)

    def test_get_current_funding_rate_valid_symbol(self, market: Market):
        response = market.get_current_funding_rate("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_current_funding_rate_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_current_funding_rate("BTCUSDT")

    #TODO: add more test for this functions for args: start_time, end_time
    def test_get_funding_rate_history_valid_symbol(self, market: Market):
        response = market.get_funding_rate_history("BTC-USDT")
        assert isinstance(response, list)

    def test_get_funding_rate_history_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_funding_rate_history("BTCUSDT")

    def test_get_funding_rate_history_invalid_limit(self, market: Market):
        with pytest.raises(ClientError):
            market.get_funding_rate_history("BTCUSDT", limit=123456)

    #TODO: add more test for this functions for args: start_time, end_time
    def test_get_k_line_data_valid(self, market: Market):
        response = market.get_k_line_data("BTC-USDT", "1m")
        assert isinstance(response, dict)

    def test_get_k_line_data_invalid_symbol(self, market: Market):
        with pytest.raises(ClientError):
            market.get_k_line_data("BTCUSDT", "1m")

    def test_get_k_line_data_invalid_interval(self, market: Market):
        with pytest.raises(ClientError):
            market.get_k_line_data("BTC-USDT", "1Y")

    def test_get_k_line_data_invalid_limit(self, market: Market):
        with pytest.raises(ClientError):
            market.get_k_line_data("BTC-USDT", "1m", limit=123456)

    def test_get_swap_open_positions_valid(self, market: Market):
        response = market.get_swap_open_positions("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_swap_open_positions_invalid(self, market: Market):
        with pytest.raises(ClientError):
            market.get_swap_open_positions("BTCUSDT")

    def test_get_ticker_valid(self, market: Market):
        response = market.get_ticker()
        assert isinstance(response, list)

    def test_get_ticker_valid_symbol(self, market: Market):
        response = market.get_ticker("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_ticker_invalid(self, market: Market):
        with pytest.raises(ClientError):
            market.get_ticker("BTCUSDT")
