from typing import Any

from bingx._http_manager import _HTTPManager
from bingx.perpetual.v2.types import HistoryOrder


class Standard(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def get_all_positions(self) -> list[dict[str, Any]]:
        """

        https://bingx-api.github.io/docs/standard/contract-interface.html#position
        """

        endpoint =  "/openApi/contract/v1/allPosition"

        response = self.__http_manager.get(endpoint)
        return response.json()["data"]

    def get_orders_history(self, order: HistoryOrder) -> list[dict[str, Any]]:
        """

        https://bingx-api.github.io/docs/standard/contract-interface.html#historical-order
        """

        endpoint =  "/openApi/contract/v1/allOrders"
        payload = order.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_account_details(self) -> list[dict[str, Any]]:
        """

        https://bingx-api.github.io/docs/standard/contract-interface.html#query-standard-contract-balance
        """

        endpoint = "/openApi/contract/v1/balance"

        response = self.__http_manager.get(endpoint)
        return response.json()["data"]
