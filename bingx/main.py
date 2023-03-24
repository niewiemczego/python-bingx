from bingX.perpetual.v1 import PerpetualV1
from bingX.perpetual.v2 import PerpetualV2
from bingX.spot import Spot
from bingX.standard import Standard


class BingX:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.perpetual_v1 = PerpetualV1(api_key, secret_key)
        self.perpetual_v2 = PerpetualV2(api_key, secret_key)
        self.spot = Spot(api_key, secret_key)
        self.standard = Standard(api_key, secret_key)

