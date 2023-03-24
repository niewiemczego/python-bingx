from typing import Any

from bingX._http_manager import _HTTPManager
from bingX.perpetual.v2.types import (
    ForceOrder,
    HistoryOrder,
    MarginType,
    Order,
    PositionSide,
)

#  symbol: strf
#     type: OrderType
#     side: Side
#     position_side: PositionSide = PositionSide.LONG
#     price: float | None = None
#     quantity: float | None = None
#     stop_price: float | None = None
#     recv_window: int | None = None

    # SELL - SHORT -> OPEN SHORT POSITION
    # BUY - LONG -> OPEN LONG POSITION
    # SELL - LONG -> CLOSE LONG POSITION
    # BUY - SHORT -> CLOSE SHORT POSITION
    # res = bingx_exchange.set_leverage("DOGE-USDT", PositionSide.SHORT, 2)
    # print(res)
    # order_id = bingx_exchange.create_order(Order(
    #     PositionSide.SHORT,
    #     "DOGE-USDT",
    #     40.0,
    #     0.1,
    #     2
    # ))
    # print(order_id) # 1638669174471397376 , 1638669258827239424

    # order_id = bingx_exchange.close_order(Order(
    #     PositionSide.SHORT,
    #     "DOGE-USDT",
    #     5.0,
    #     0.1,
    #     2
    # ))
    # print(order_id)

class Trade(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def create_order(self, order: Order) -> dict[str, Any]:
        """
        The current account places an order on the specified symbol contract.

        examples:
        - create long: Order(symbol="DOGE-USDT", side=Side.BUY, position_side=PositionSide.LONG, quantity=100.0)
        - create short: Order(symbol="DOGE-USDT", side=Side.SELL, position_side=PositionSide.SHORT, quantity=100.0)


        https://bingx-api.github.io/docs/swapV2/trade-api.html#_1-trade-order
        """

        endpoint = "/openApi/swap/v2/trade/order"
        payload = order.to_dict()

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def close_order(self, order: Order) -> dict[str, Any]:
        """
        The current account closes an order on the specified symbol contract. This is custom method which is not documented in the official API.

        examples:
        - close long: Order(symbol="DOGE-USDT", side=Side.SELL, position_side=PositionSide.LONG, quantity=100.0)
        - close short: Order(symbol="DOGE-USDT", side=Side.BUY, position_side=PositionSide.SHORT, quantity=100.0)
        """

        endpoint = "/openApi/swap/v2/trade/order"
        payload = order.to_dict()

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def bulk_create_order(self, orders: list[Order], recvWindow: int | None = None) -> dict[str, Any]:
        """
        The current account performs batch order operations on the specified symbol contract.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_2-bulk-order
        """

        endpoint = "/openApi/swap/v2/trade/batchOrders"
        payload = {"batchOrders": [order.to_dict() for order in orders]} if recvWindow is None else {"batchOrders": [order.to_dict() for order in orders], "recvWindow": recvWindow}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def close_all_positions(self, recvWindow: int | None = None) -> dict[str, Any]:
        """
        One-click liquidation of all positions under the current account. Note that one-click liquidation is triggered by a market order.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_3-one-click-close-all-positions
        """

        endpoint = "/openApi/swap/v2/trade/closeAllPositions"
        payload = {} if recvWindow is None else {"recvWindow": recvWindow}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def cancel_order(self, order_id: int, symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Cancel an order that the current account is in the current entrusted state.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_4-cancel-an-order
        """

        endpoint = "/openApi/swap/v2/trade/order"
        payload = {"orderId": order_id, "symbol": symbol} if recvWindow is None else {"orderId": order_id, "symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.delete(endpoint, payload)
        return response.json()["data"]

    def cancel_batch_orders(self, order_ids: list[int], symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Batch cancellation of some of the orders whose current account is in the current entrusted state.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_5-cancel-a-batch-of-orders
        """

        endpoint = "/openApi/swap/v2/trade/batchOrders"
        payload = {"orderIdList": order_ids, "symbol": symbol} if recvWindow is None else {"orderIdList": order_ids, "symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.delete(endpoint, payload)
        return response.json()["data"]

    def cancel_all_orders(self, symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Cancel all orders in the current entrusted state of the current account.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_6-cancel-all-orders
        """

        endpoint = "/openApi/swap/v2/trade/allOpenOrders"
        payload = {"symbol": symbol} if recvWindow is None else {"symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.delete(endpoint, payload)
        return response.json()["data"]

    def get_open_orders(self, symbol: str | None = None, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Query all orders that the user is currently entrusted with.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_7-query-all-current-pending-orders
        """

        endpoint = "/openApi/swap/v2/trade/openOrders"
        if symbol is None:
            payload = {} if recvWindow is None else {"recvWindow": recvWindow}
        else:
            payload = {"symbol": symbol} if recvWindow is None else {"symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_order(self, order_id: int, symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Query order details

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_8-query-order
        """

        endpoint = "/openApi/swap/v2/trade/order"
        payload = {"symbol": symbol, "orderId": order_id} if recvWindow is None else {"symbol": symbol, "orderId": order_id, "recvWindow": recvWindow}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_margin_mode(self, symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Query the user's margin mode on the specified symbol contract: isolated or cross.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_9-query-margin-mode
        """

        endpoint = "/openApi/swap/v2/trade/marginType"
        payload = {"symbol": symbol} if recvWindow is None else {"symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def change_margin_mode(self, symbol: str, margin_type: MarginType, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Change the user's margin mode on the specified symbol contract: isolated margin or cross margin.]

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_10-switch-margin-mode
        """

        endpoint = "/openApi/swap/v2/trade/marginType"
        payload = {"symbol": symbol, "marginType": margin_type.value} if recvWindow is None else {"symbol": symbol, "marginType": margin_type.value, "recvWindow": recvWindow}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_leverage(self, symbol: str, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Query the opening leverage of the user in the specified symbol contract.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_11-query-leverage
        """

        endpoint = "/openApi/swap/v2/trade/leverage"
        payload = {"symbol": symbol} if recvWindow is None else {"symbol": symbol, "recvWindow": recvWindow}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def change_leverage(self, symbol: str, position_side: PositionSide, leverage: int, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Adjust the user's opening leverage in the specified symbol contract.

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_12-switch-leverage
        """

        endpoint = "/openApi/swap/v2/trade/leverage"
        payload = {"symbol": symbol, "side": position_side.value, "leverage": leverage} if recvWindow is None else {"symbol": symbol, "side": position_side.value, "leverage": leverage, "recvWindow": recvWindow}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()

    def get_force_orders(self, force_order: ForceOrder) -> dict[str, Any]:
        """
        Query the user's forced liquidation order. If "autoCloseType" is not passed, both forced liquidation orders and ADL liquidation orders will be returned.
        If "startTime" is not passed, only the data within 7 days before "endTime" will be returned

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_13-user-s-force-orders
        """

        endpoint = "/openApi/swap/v2/trade/forceOrders"
        payload = force_order.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_orders_history(self, history_order: HistoryOrder) -> dict[str, Any]:
        """
        Query the user's historical orders (order status is completed or canceled). The maximum query time range shall not exceed 7 days.
        Query data within the last 7 days by default

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_14-user-s-history-orders
        """

        endpoint = "/openApi/swap/v2/trade/allOrders"
        payload = history_order.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def change_isolated_margin(self, symbol: str, amount: float, type: int, position_side: PositionSide = PositionSide.LONG, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Adjust the isolated margin funds for the positions in the isolated position mode.

        :param symbol: The symbol you want to trade
        :param amount: The amount of margin to be added or removed
        :param type: 1 for increase, 2 for decrease
        :param position_side: PositionSide = PositionSide.LONG
        :param recvWindow: The number of milliseconds the request is valid for

        https://bingx-api.github.io/docs/swapV2/trade-api.html#_15-adjust-isolated-margin
        """

        endpoint = "/openApi/swap/v2/trade/positionMargin"
        payload = {"symbol": symbol, "amount": amount, "type": type, "positionSide": position_side.value} if recvWindow is None else {"symbol": symbol, "amount": amount, "type": type, "positionSide": position_side.value, "recvWindow": recvWindow}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()
