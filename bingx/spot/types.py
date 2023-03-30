from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from bingX._helpers import DictMixin
from bingX.exceptions import HistoryOrderException, OrderException


class TransferType(Enum):
    FUND_SFUTURES = "FUND_SFUTURES"
    SFUTURES_FUND = "SFUTURES_FUND"
    FUND_PFUTURES = "FUND_PFUTURES"
    PFUTURES_FUND = "PFUTURES_FUND"
    SFUTURES_PFUTURES = "SFUTURES_PFUTURES"
    PFUTURES_SFUTURES = "PFUTURES_SFUTURES"


class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"


class TimeInForce(Enum):
    IOC = "IOC"
    POC = "POC"


@dataclass
class Order(DictMixin):
    symbol: str
    side: Side
    type: OrderType
    type_in_force: TimeInForce | None = None
    quantity: float | None = None
    quote_order_qty: float | None = None
    price: float | None = None
    recvWindow: int | None = None

    def __post_init__(self):
        if self.type == OrderType.LIMIT:
            if (self.quantity is None) or (self.price is None):
                raise OrderException("LIMIT order must have quantity/quote_order_qty and price")
        elif self.type == OrderType.MARKET:
            if self.side == Side.BUY:
                if self.quote_order_qty is None:
                    raise OrderException("BUY MARKET order must have quote_order_qty")
            elif self.side == Side.SELL:
                if self.quantity is None:
                    raise OrderException("SELL MARKET order must have quantity")


@dataclass
class HistoryOrder(DictMixin):
    symbol: str
    order_id: int | None = None
    start_time: int | None = None
    end_time: int | None = None
    page_index: int | None = None
    page_size: int | None = None
    recv_window: int | None = None

    def __post_init__(self):
        if self.page_index is not None and self.page_index > 0:
            raise(HistoryOrderException("page_index must be greater than 0"))
        if self.page_size is not None and self.page_size <= 100:
            raise(HistoryOrderException("page_size must be less or equal to 100"))


@dataclass
class UniversalTransfer(DictMixin):
    type: TransferType
    asset: str | None = None
    amount: float | None = None
    recv_window: int | None = None


@dataclass
class HistoryTransfer(DictMixin):
    type: TransferType
    start_time: int | None = None
    end_time: int | None = None
    current: int | None = None
    size: int | None = None
    recv_window: int | None = None


@dataclass
class HistoryDeposit(DictMixin):
    coin: str | None = None
    status: int | None = None
    start_time: int | None = None
    end_time: int | None = None
    offset: int = 0
    limit: int = 1000
    recv_window: int | None = None

    def __post_init__(self):
        if self.offset is not None and self.offset < 0:
            raise(HistoryOrderException("offset must be greater than 0"))


@dataclass
class HistoryWithdraw(DictMixin):
    coin: str | None = None
    withdraw_order_id: str | None = None
    status: int | None = None
    start_time: int | None = None
    end_time: int | None = None
    offset: int = 0
    limit: int = 1000
    recv_window: int | None = None

    def __post_init__(self):
        if self.offset is not None and self.offset < 0:
            raise(HistoryOrderException("offset must be greater than 0"))
