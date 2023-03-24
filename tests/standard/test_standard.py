import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.perpetual.v2.types import HistoryOrder
from bingX.standard import Standard

load_dotenv()

class TestStandard:
    @pytest.fixture
    def standard(self) -> Standard:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Standard(api_key, secret_key)

    def test_get_all_positions_valid(self, standard: Standard):
        response = standard.get_all_positions()
        assert isinstance(response, list)

    def test_get_orders_history_valid_symbol(self, standard: Standard):
        response = standard.get_orders_history(HistoryOrder("BTC-USDT"))
        assert isinstance(response, list)

    def test_get_account_details(self, standard: Standard):
        response = standard.get_account_details()
        assert isinstance(response, list)