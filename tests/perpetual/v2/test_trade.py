import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.perpetual.v2.trade import Trade
from bingX.perpetual.v2.types import (
    ForceOrder,
    HistoryOrder,
    MarginType,
    Order,
    OrderType,
    PositionSide,
    Side,
)

load_dotenv()

class TestTrade:
    @pytest.fixture
    def trade(self) -> Trade:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Trade(api_key, secret_key)

    # def test_create_order(self, trade: Trade):
    #     order = Order("DOGEUSDT", OrderType.MARKET, Side.BUY, PositionSide.LONG, quantity=10.0)
    #     response = trade.create_order(order)
    #     assert isinstance(response, dict)
    #     assert response["data"]["order"]["symbol"] == "DOGEUSDT"
    #     assert response["data"]["order"]["orderType"] == "MARKET"
    #     assert response["data"]["order"]["side"] == "BUY"
    #     assert response["data"]["order"]["positionSide"] == "LONG"