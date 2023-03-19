import os

import pytest
from dotenv import load_dotenv

from bingx_client._exceptions import ClientError
from bingx_client.perpetual.v2.trade import Trade

load_dotenv()

class TestTrade:
    @pytest.fixture
    def trade(self) -> Trade:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Trade(api_key, secret_key)
