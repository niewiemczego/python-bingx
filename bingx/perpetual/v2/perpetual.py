from bingx.perpetual.v2.account import Account
from bingx.perpetual.v2.market import Market
from bingx.perpetual.v2.other import Other
from bingx.perpetual.v2.trade import Trade


class PerpetualV2:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.account = Account(api_key, secret_key)
        self.market = Market(api_key, secret_key)
        self.trade = Trade(api_key, secret_key)
        self.other = Other(api_key, secret_key)
