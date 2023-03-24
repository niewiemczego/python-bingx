import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.perpetual.v2.account import Account
from bingX.perpetual.v2.types import IncomeType, ProfitLossFundFlow

load_dotenv()

class TestAccount:
    @pytest.fixture
    def account(self) -> Account:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Account(api_key, secret_key)

    def test_get_details_valid(self, account: Account):
        response = account.get_details()
        assert isinstance(response, dict)

    def test_get_swap_positions_valid(self, account: Account):
        response = account.get_swap_positions()
        assert isinstance(response, list)

    def test_get_swap_positions_valid_symbol(self, account: Account):
        response = account.get_swap_positions("BTC-USDT")
        assert isinstance(response, dict)

    def test_get_swap_positions_valid_symbol(self, account: Account):
        with pytest.raises(ClientError):
            account.get_swap_positions("BTCUSDT")

    def test_get_profit_loss_fund_flow_valid(self, account: Account):
        response = account.get_profit_loss_fund_flow(ProfitLossFundFlow())
        assert isinstance(response, list)

    def test_get_profit_loss_fund_flow_valid_symbol(self, account: Account):
        profit_loss_fund_flow = ProfitLossFundFlow("BTC-USDT")
        response = account.get_profit_loss_fund_flow(profit_loss_fund_flow)
        assert isinstance(response, list)

    def test_get_profit_loss_fund_flow_invalid_symbol(self, account: Account):
        profit_loss_fund_flow = ProfitLossFundFlow("BTCUSDT")
        response = account.get_profit_loss_fund_flow(profit_loss_fund_flow)
        assert response is None

    def test_get_profit_loss_fund_flow_valid_income_type(self, account: Account):
        profit_loss_fund_flow = ProfitLossFundFlow("BTC-USDT", IncomeType.FUNDING_FEE)
        response = account.get_profit_loss_fund_flow(profit_loss_fund_flow)
        assert isinstance(response, list)

    def test_get_profit_loss_fund_flow_invalid_income_type(self):
        with pytest.raises(AttributeError):
            ProfitLossFundFlow("BTC-USDT", IncomeType.INVALID)

    def test_get_profit_loss_fund_flow_invalid_limit(self, account: Account):
        with pytest.raises(ClientError):
            profit_loss_fund_flow = ProfitLossFundFlow("BTC-USDT", IncomeType.FUNDING_FEE, limit=123456)
            account.get_profit_loss_fund_flow(profit_loss_fund_flow)
