from typing import Any

from bingx_client._http_manager import _HTTPManager
from bingx_client.spot._types import HistoryOrder, Order


class Market:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def get_symbols(self, symbol: str | None = None) -> list[dict[str, Any]]:
        """
        Get the list of symbols and their details

        :param symbol: The symbol of the trading pair
        :return: A dictionary of symbols and their associated information.

        https://bingx-api.github.io/docs/spot/market-interface.html#query-symbols
        """

        endpoint = "/openApi/spot/v1/common/symbols"
        payload = {} if symbol is None else {"symbol": symbol}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_transaction_records(self, symbol: str, limit: int = 100) -> list[dict[str, Any]]:
        """
        Get the transaction records of a symbol

        :param symbol: The symbol of the trading pair
        :param limit: The number of transaction records to return. Default 100, max 100

        https://bingx-api.github.io/docs/spot/market-interface.html#query-transaction-records
        """

        endpoint = "/openApi/spot/v1/market/trades"
        payload = {"symbol": symbol, "limit": limit}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_depth_details(self, symbol: str, limit: int = 20) -> list[list[str]]:
        """
        Get the depth details for a given symbol

        :param symbol: The symbol of the trading pair
        :param limit: The number of transaction records to return. Default 20, max 100

        https://bingx-api.github.io/docs/spot/market-interface.html#query-depth-information
        """

        endpoint = "/openApi/spot/v1/market/depth"
        payload = {"symbol": symbol, "limit": limit}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]
