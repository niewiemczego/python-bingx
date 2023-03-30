from dataclasses import dataclass
from enum import Enum

from bingX._helpers import DictMixin
from bingX.exceptions import HistoryOrderException, OrderException


class Side(Enum):
    BID = "Bid"
    ASK = "Ask"


class OrderType(Enum):
    LIMIT = "Limit"
    MARKET = "Market"


class TimeInForce(Enum):
    IOC = "IOC"
    POC = "POC"


class Action(Enum):
    OPEN = "Open"
    CLOSE = "Close"


class MarginType(Enum):
    ISOLATED = "Isolated"
    CROSSED = "Crossed"


class PositionSide(Enum):
    LONG = "Long"
    SHORT = "Short"


@dataclass
class Order(DictMixin):
    symbol: str
    side: Side
    entrust_price: float
    entrust_volume: float
    type: OrderType
    action: Action
    taker_profit_price: float | None = None
    stop_loss_price: float | None = None
