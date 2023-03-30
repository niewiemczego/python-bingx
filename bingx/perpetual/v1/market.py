from typing import Any

from bingX._http_manager import _HTTPManager


class Market:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def get_contract_info(self) -> list[dict[str, Any]]:
        """
        Get the contract information of the swap contract

        https://bingx-api.github.io/docs/swap/market-api.html#_1-contract-information
        """

        endpoint =  "/api/v1/market/getAllContracts"

        response = self.__http_manager.get(endpoint)
        return response.json()["data"]

    def get_latest_price_of_trading_pair(self, symbol: str) -> dict[str, Any]:
        """
        It returns the latest price of a trading pair. If no transaction pair parameters are sent, all transaction pair information will be returned

        :param symbol: The trading pair you want to get the latest price of

        https://bingx-api.github.io/docs/swap/market-api.html#_2-get-latest-price-of-a-trading-pair
        """

        endpoint =  "/api/v1/market/getLatestPrice"

        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_market_depth(self, symbol: str, level: int = 5) -> dict[str, Any]:
        """
        It returns the market depth of a given symbol

        :param symbol: The symbol you want to get the market depth for
        :param level: Number of levels

        https://bingx-api.github.io/docs/swap/market-api.html#_3-get-market-depth
        """

        endpoint =  "/api/v1/market/getMarketDepth"

        payload = {"symbol": symbol.upper(), "level": level}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_latest_trade_of_trading_pair(self, symbol: str) -> dict[str, Any]:
        """
        It returns the latest trade of a trading pair.

        :param symbol: The trading pair you want to get the latest trades for

        https://bingx-api.github.io/docs/swap/market-api.html#_4-the-latest-trade-of-a-trading-pair
        """

        endpoint =  "/api/v1/market/getMarketTrades"

        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_current_funding_rate(self, symbol: str) -> dict[str, Any]:
        """
        Get the current funding rate for a given symbol

        :param symbol: The symbol you want to get the funding rate for. If you don't specify a symbol, you'll get the funding rate for all symbols

        https://bingx-api.github.io/docs/swap/market-api.html#_5-current-funding-rate
        """

        endpoint =  "/api/v1/market/getLatestFunding"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_funding_rate_history(self, symbol: str) -> dict[str, Any]:
        """
        It returns the funding rate history for a given symbol.

        :param symbol: The symbol you want to get the funding rate for

        https://bingx-api.github.io/docs/swap/market-api.html#_6-funding-rate-history
        """

        endpoint = "/api/v1/market/getHistoryFunding"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_k_line_data(self, symbol: str, kline_type: str) -> dict[str, Any]:
        """
        Get the latest Kline Data.

        :param symbol: The trading pair you want to get the Kline data for
        :param kline_type: The type of K-Line (minutes, hours, weeks etc.)

        https://bingx-api.github.io/docs/swap/market-api.html#_7-get-k-line-data
        """

        endpoint = "/api/v1/market/getLatestKline"
        payload = {"symbol": symbol.upper(), "klineType": kline_type}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_k_line_data_history(self, symbol: str, kline_type: str, start_time: int, end_time: int) -> dict[str, Any]:
        """
        Get the K-Line history data of the trading price over a certain period of time.

        :param symbol: The trading pair you want to get the Kline data for
        :param kline_type: The type of K-Line (minutes, hours, weeks etc.)
        :param start_time: The start time of the Kline data you want to get
        :param end_time: The end time of the Kline data you want to get

        https://bingx-api.github.io/docs/swap/market-api.html#_8-k-line-data-history
        """

        endpoint = "/api/v1/market/getHistoryKlines"
        payload = {"symbol": symbol.upper(), "klineType": kline_type, "startTime": start_time, "endTime": end_time}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_swap_open_positions(self, symbol: str) -> dict[str, Any]:
        """
        It returns the open positions for a given symbol.

        :param symbol: The symbol you want to get the open interest for

        https://bingx-api.github.io/docs/swap/market-api.html#_9-get-swap-open-positions
        """

        endpoint = "/api/v1/market/getOpenPositions"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]

    def get_ticker(self, symbol: str | None = None) -> dict[str, Any] :
        """
        It returns the ticker for a given symbol.
        If no transaction pair parameters are sent, all transaction pair information will be returned

        :param symbol: The symbol you want to get the ticker for. If you don't specify a symbol, you'll getthe ticker for all symbols

        https://bingx-api.github.io/docs/swap/market-api.html#_10-get-ticker
        """

        endpoint = "/api/v1/market/getTicker"
        payload = {} if symbol is None else {"symbol": symbol.upper()}

        response = self.__http_manager.get(endpoint, payload)
        return response.json()["data"]
