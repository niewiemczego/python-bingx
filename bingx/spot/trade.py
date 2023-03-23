from typing import Any

from bingx._http_manager import _HTTPManager
from bingx.spot.types import HistoryOrder, Order


class Trade:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def create_order(self, order: Order) -> dict[str, Any]:
        """
        The current account places an order on the specified symbol contract. For limit orders, price is required.
        For limit orders, either quantity or quoteOrderQty is required. When two parameters are passed at the same time, the server uses the parameter quantity first.
        For buy-side market orders, quoteOrderQty is required. For sell-side market orders, quantity is required.
        Orders created by the interface will not be displayed on the APP and web pages.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_1-trade-order
        """

        endpoint = "/openApi/spot/v1/trade/order"
        payload = order.to_dict()

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def cancel_order(self, order_id: int, symbol: str, recv_window: int | None = None) -> dict[str, Any]:
        """
        Cancel an order that the current account is in the current entrusted state.

        https://bingx-api.github.io/docs/spot/trade-interface.html#cancel-an-order
        """

        endpoint = "/openApi/spot/v1/trade/cancel"
        payload = {"symbol": symbol, "orderId": order_id} if recv_window is None else {"orderId": order_id, "symbol": symbol, "recvWindow": recv_window}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_order(self, order_id: int, symbol: str, recv_window: int | None = None) -> dict[str, Any]:
        """
        Query order details

        https://bingx-api.github.io/docs/spot/trade-interface.html#query-orders
        """

        endpoint = "/openApi/spot/v1/trade/query"
        payload = {"symbol": symbol, "orderId": order_id} if recv_window is None else {"symbol": symbol, "orderId": order_id, "recvWindow": recv_window}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_open_orders(self, symbol: str | None = None, recv_window: int | None = None) -> dict[str, Any]:
        """
        Query all orders that the user is currently entrusted with.

        https://bingx-api.github.io/docs/spot/trade-interface.html#query-open-orders
        """

        endpoint = "/openApi/spot/v1/trade/openOrders"
        payload = {"symbol": symbol} if recv_window is None else {"symbol": symbol, "recvWindow": recv_window}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_orders_history(self, history_order: HistoryOrder) -> dict[str, Any]:
        """
        Query the user's historical orders. If orderId is set, orders >= orderId. Otherwise, the most recent orders will be returned.
        If startTime and endTime are provided, orderId is not required.

        https://bingx-api.github.io/docs/spot/trade-interface.html#query-order-history
        """

        endpoint = "/openApi/spot/v1/trade/historyOrders"
        payload = history_order.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_assets(self, recv_window: int | None = None) -> dict[str, Any]:
        """
        Query the user's asset information.

        https://bingx-api.github.io/docs/spot/trade-interface.html#query-assets
        """

        endpoint = "/openApi/spot/v1/account/balance"
        payload = {} if recv_window is None else {"recvWindow": recv_window}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]
