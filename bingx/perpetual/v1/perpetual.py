from bingX.perpetual.v1.account import Account
from bingX.perpetual.v1.market import Market
from bingX.perpetual.v1.other import Other
from bingX.perpetual.v1.trade import Trade


class PerpetualV1:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.account = Account(api_key, secret_key)
        self.market = Market(api_key, secret_key)
        self.trade = Trade(api_key, secret_key)
        self.other = Other(api_key, secret_key)
