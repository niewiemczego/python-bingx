from bingx.perpetual.v1 import PerpetualV1
from bingx.perpetual.v2 import PerpetualV2
from bingx.spot import Spot
from bingx.standard import Standard


class BingX:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.perpetual_v1 = PerpetualV1(api_key, secret_key)
        self.perpetual_v2 = PerpetualV2(api_key, secret_key)
        self.spot = Spot(api_key, secret_key)
        self.standard = Standard(api_key, secret_key)

