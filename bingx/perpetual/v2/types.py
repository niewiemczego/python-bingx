from dataclasses import dataclass
from enum import Enum
from typing import Any

from bingX._helpers import DictMixin
from bingX.exceptions import OrderException


class MarginType(Enum):
    ISOLATED = "ISOLATED"
    CROSSED = "CROSSED"


class PositionSide(Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP_MARKET = "STOP_MARKET"
    TAKE_PROFIT_MARKET = "TAKE_PROFIT_MARKET"
    TRIGGER_LIMIT = "TRIGGER_LIMIT"
    TRIGGER_MARKET = "TRIGGER_MARKET"


@dataclass
class Order(DictMixin):
    symbol: str
    side: Side
    position_side: PositionSide
    quantity: float | None = None
    type: OrderType = OrderType.MARKET
    price: float | None = None
    stop_price: float | None = None
    recv_window: int | None = None

    def __post_init__(self):
        if self.type == OrderType.LIMIT:
            if (self.quantity is None) or (self.price is None):
                raise OrderException("LIMIT order must have quantity and price")
        elif self.type == OrderType.MARKET:
            if self.quantity is None:
                raise OrderException("MARKET order must have quantity")
        elif self.type == OrderType.TRIGGER_LIMIT:
            if (self.quantity is None) or (self.stop_price is None) or (self.price is None):
                raise OrderException("TRIGGER_LIMIT order must have quantity, stop_price and price")
        elif self.type in [OrderType.STOP_MARKET, OrderType.TAKE_PROFIT_MARKET, OrderType.TRIGGER_MARKET]:
            if (self.quantity is None) or (self.stop_price is None):
                raise OrderException("STOP_MARKET, TAKE_PROFIT_MARKET and TRIGGER_MARKET orders must have quantity and stop_price")


class IncomeType(Enum):
    TRANSFER = "TRANSFER"
    REALIZED_PNL = "REALIZED_PNL"
    FUNDING_FEE = "FUNDING_FEE"
    TRADING_FEE = "TRADING_FEE"
    INSURANCE_CLEAR = "INSURANCE_CLEAR"
    TRIAL_FUND = "TRIAL_FUND"
    ADL = "ADL"
    SYSTEM_DEDUCTION = "SYSTEM_DEDUCTION"


@dataclass
class ProfitLossFundFlow(DictMixin):
    symbol: str | None = None
    income_type: IncomeType | None = None
    start_time: int | None = None
    end_time: int | None = None
    limit: int = 100
    recv_window: int | None = None


@dataclass
class ForceOrder(DictMixin):
    symbol: str | None = None
    auto_close_type: str | None = None
    start_time: int | None = None
    end_time: int | None = None
    limit: int = 50
    recv_window: int | None = None


@dataclass
class HistoryOrder(DictMixin):
    symbol: str
    order_id: int | None = None
    start_time: int | None = None
    end_time: int | None = None
    limit: int = 500
    recv_window: int | None = None
