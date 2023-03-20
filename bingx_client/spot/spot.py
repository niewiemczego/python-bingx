from bingx_client.spot.market import Market
from bingx_client.spot.trade import Trade
from bingx_client.spot.transfer import Transfer


class Spot:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.trade = Trade(api_key, secret_key)
        self.market = Market(api_key, secret_key)
        self.transfer = Transfer(api_key, secret_key)