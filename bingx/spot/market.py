from typing import Any

from bingX._http_manager import _HTTPManager
from bingX.spot.types import HistoryOrder, Order


class Market:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def get_symbols(self, symbol: str | None = None) -> dict[str, Any]:
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

    def get_depth_details(self, symbol: str, limit: int = 20) -> dict[str, Any]:
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

    def get_k_line_data(self, symbol: str, interval: str, start_time: int | None = None, end_time: int | None = None, limit: int = 1) -> list[dict[str, Any]] | dict[str, Any]:
        """
        Get the latest Kline Data.
        If startTime and endTime are not sent, the latest k-line data will be returned by default

        :param symbol: The trading pair you want to get the Kline data for
        :param interval: The interval of the Kline data, possible values: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 1w, 1M
        :param start_time: The start time of the Kline data, in milliseconds
        :param end_time: The end time of the Kline data, in milliseconds
        :param limit: The number of Kline data to return, maximum 1440

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Candlestick%20chart%20data
        """
        VALID_INTERVALS = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]
        if interval not in VALID_INTERVALS:
            raise ValueError("[!] INVALID INTERVAL VALUE. Valid Intervals are: ", str(VALID_INTERVALS))

        endpoint = "/openApi/spot/v2/market/kline"
        payload = {"symbol": symbol.upper(), "interval": interval, "limit": limit} if start_time is None or end_time is None else {"symbol": symbol.upper(), "interval": interval, "startTime": start_time, "endTime": end_time, "limit": limit}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]
