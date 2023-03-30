from typing import Any

from bingX._http_manager import _HTTPManager
from bingX.perpetual.v1.types import MarginType, Order, PositionSide


class Trade:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def create_order(self, order: Order) -> dict[str, Any]:
        """
        The current account places an order on the specified symbol contract.

        https://bingx-api.github.io/docs/swap/trade-api.html#_1-place-a-new-order
        """

        endpoint = "/api/v1/user/trade"
        payload = order.to_dict()

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def one_click_close_position(self, symbol: str, position_id: int) -> dict[str, Any]:
        """
        After querying the position information, you can close the position by one-click based on the position ID. Please note that the one-click closed position is traded at market price.

        https://bingx-api.github.io/docs/swap/trade-api.html#_2-one-click-close-position
        """

        endpoint = "/api/v1/user/oneClickClosePosition"
        payload = {"symbol": symbol.upper(), "positionId": position_id}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def one_click_close_all_position(self, symbol: str, position_id: int) -> dict[str, Any]:
        """
        Close all positions within the current account by one click. Please note that the one-click closed positions are traded at market price.

        https://bingx-api.github.io/docs/swap/trade-api.html#_3-one-click-close-all-positions
        """

        endpoint = "/api/v1/user/oneClickCloseAllPositions"

        response = self.__http_manager.post(endpoint)
        return response.json()["data"]

    def cancel_order(self, order_id: int, symbol: str) -> dict[str, Any]:
        """
        Cancel an order that is currently in a unfilled state

        https://bingx-api.github.io/docs/swap/trade-api.html#_4-cancel-an-order
        """

        endpoint = "/api/v1/user/cancelOrder"
        payload = {"orderId": order_id, "symbol": symbol.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def cancel_batch_orders(self, order_ids: list[int], symbol: str) -> dict[str, Any]:
        """
        Cancel a batch of orders that are currently in a unfilled state

        https://bingx-api.github.io/docs/swap/trade-api.html#_5-cancel-a-batch-of-orders
        """

        endpoint = "/api/v1/user/batchCancelOrders"
        payload = {"symbol": symbol.upper(), "oids": order_ids}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def cancel_all_orders(self) -> dict[str, Any]:
        """
        Cancel all orders that are currently in a unfilled state

        https://bingx-api.github.io/docs/swap/trade-api.html#_6-cancel-all-orders
        """

        endpoint = "/api/v1/user/cancelAll"

        response = self.__http_manager.post(endpoint)
        return response.json()["data"]

    def get_unfilled_order_acquisition(self, symbol: str) -> dict[str, Any]:
        """
        Query the details of unfilled orders within the current account over a certain period of time

        https://bingx-api.github.io/docs/swap/trade-api.html#_7-unfilled-order-acquisition
        """

        endpoint = "/api/v1/user/pendingOrders"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_order(self, order_id: int, symbol: str) -> dict[str, Any]:
        """
        Query order details

        https://bingx-api.github.io/docs/swap/trade-api.html#_8-query-order-details
        """

        endpoint = "/api/v1/user/queryOrderStatus"
        payload = {"symbol": symbol.upper(), "orderId": order_id}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_margin_mode(self, symbol: str) -> dict[str, Any]:
        """
        Query the user's margin mode on the specified symbol contract: isolated or cross.

        https://bingx-api.github.io/docs/swap/trade-api.html#_9-query-margin-mode
        """

        endpoint = "/api/v1/user/getMarginMode"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def change_margin_mode(self, symbol: str, margin_type: MarginType) -> dict[str, Any]:
        """
        Change the user's margin mode on the specified symbol contract: isolated margin or cross margin.]

        https://bingx-api.github.io/docs/swap/trade-api.html#_10-switch-margin-mode
        """

        endpoint = "/api/v1/user/setMarginMode"
        payload = {"symbol": symbol, "marginMode": margin_type.value}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_leverage(self, symbol: str) -> dict[str, Any]:
        """
        Query the opening leverage of the user in the specified symbol contract.

        https://bingx-api.github.io/docs/swap/trade-api.html#_11-query-leverage
        """

        endpoint = "/api/v1/user/getLeverage"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def change_leverage(self, symbol: str, position_side: PositionSide, leverage: int, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Switch the leverage size of a certain trading pair for long or short positions

        https://bingx-api.github.io/docs/swap/trade-api.html#_12-switch-leverage
        """

        endpoint = "/api/v1/user/setLeverage"
        payload = {"symbol": symbol.upper(), "side": position_side.value, "leverage": leverage}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_force_orders(self, symbol: str, auto_close_type, last_order_id: int, length: int) -> dict[str, Any]:
        """
        Query the user's forced liquidation order

        https://bingx-api.github.io/docs/swap/trade-api.html#_13-user-s-force-orders
        """

        endpoint = "/api/v1/user/forceOrders"
        payload = {"symbol": symbol.upper(), "autoCloseType": auto_close_type, "lastOrderId": last_order_id, "length": length}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_orders_history(self, last_order_id: int, length: int, symbol: str | None = None) -> dict[str, Any]:
        """
        Query the user's historical orders (order status is completed or canceled). The maximum query time range shall not exceed 7 days.
        Query data within the last 7 days by default

        https://bingx-api.github.io/docs/swap/trade-api.html#_14-user-s-history-orders
        """

        endpoint = "/api/v1/user/historyOrders"
        payload = {"lastOrderId": last_order_id, "length": length} if symbol is None else {"symbol": symbol, "lastOrderId": last_order_id, "length": length}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def place_stop_order(self, position_id: str, entrust_volume: float, order_id: str | None = None, stop_loss_price: float | None = None, take_profit_price: float | None = None) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/swap/trade-api.html#_15-place-a-stop-order
        """

        endpoint = "/api/v1/user/stopOrder"
        payload = {"positionId": position_id, "entrustVolume": entrust_volume, "orderId": order_id, "stopLossPrice": stop_loss_price, "takeProfitPrice": take_profit_price}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def cancel_stop_order(self, order_id: str) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/swap/trade-api.html#_16-cancel-stop-order
        """

        endpoint = "/api/v1/user/cancelStopOrder"
        payload = {"orderId": order_id}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_stop_orders(self, symbol: str) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/swap/trade-api.html#_17-query-stop-orders
        """

        endpoint = "/api/v1/user/pendingStopOrders"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_history_stop_orders(self, symbol: str, last_order_id: int, lenght: int) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/swap/trade-api.html#_18-query-history-stop-orders
        """

        endpoint = "/api/v1/user/historyStopOrders"
        payload = {"symbol": symbol.upper(), "lastOrderId": last_order_id, "length": lenght}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]