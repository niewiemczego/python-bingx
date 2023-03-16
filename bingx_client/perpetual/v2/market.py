from typing import Any

from bingx_client._http_manager import _HTTPManager


class Market(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def get_contract_info(self) -> dict[str, Any]:
        """
        Get the contract information of the swap contract

        https://bingx-api.github.io/docs/swapV2/market-api.html#_1-contract-information
        """

        endpoint =  "/openApi/swap/v2/quote/contracts"

        response = self.get(endpoint)
        return response.json()

    def get_latest_price_of_trading_pair(self, symbol: str | None = None) -> dict[str, Any]:
        """
        It returns the latest price of a trading pair. If no transaction pair parameters are sent, all transaction pair information will be returned

        :param symbol: The trading pair you want to get the latest price of

        https://bingx-api.github.io/docs/swapV2/market-api.html#_2-get-latest-price-of-a-trading-pair
        """

        endpoint =  "/openApi/swap/v2/quote/price"

        payload = {} if symbol is None else {"symbol": symbol.upper()}

        response = self.get(endpoint, payload)
        return response.json()

    def get_market_depth(self, symbol: str, limit: int = 20) -> dict[str, Any]:
        """
        It returns the market depth of a given symbol

        :param symbol: The symbol you want to get the market depth for
        :param limit: The number of price levels to return, optional value:[5, 10, 20, 50, 100, 500, 1000]

        https://bingx-api.github.io/docs/swapV2/market-api.html#_3-get-market-depth
        """

        endpoint =  "/openApi/swap/v2/quote/depth"

        payload = {"symbol": symbol.upper(), "limit": limit}

        response = self.get(endpoint, payload)
        return response.json()

    def get_latest_trade_of_trading_pair(self, symbol: str, limit: int = 500) -> dict[str, Any]:
        """
        It returns the latest trade of a trading pair.

        :param symbol: The trading pair you want to get the latest trades for
        :param limit: The number of trades to return, maximum 1000

        https://bingx-api.github.io/docs/swapV2/market-api.html#_4-the-latest-trade-of-a-trading-pair
        """

        endpoint =  "/openApi/swap/v2/quote/trades"

        payload = {"symbol": symbol.upper(), "limit": limit}

        response = self.get(endpoint, payload)
        return response.json()

    def get_current_funding_rate(self, symbol: str | None = None) -> dict[str, Any]:
        """
        Get the current funding rate for a given symbol

        :param symbol: The symbol you want to get the funding rate for. If you don't specify a symbol, you'll get the funding rate for all symbols

        https://bingx-api.github.io/docs/swapV2/market-api.html#_5-current-funding-rate
        """

        endpoint =  "/openApi/swap/v2/quote/premiumIndex"
        payload = {} if symbol is None else {"symbol": symbol.upper()}

        response = self.get(endpoint, payload)
        return response.json()

    def get_funding_rate_history(self, symbol: str, start_time: int | None = None, end_time: int | None = None, limit: int = 100) -> dict[str, Any]:
        """
        It returns the funding rate history for a given symbol.
        If both startTime and endTime are not sent, return the latest limit data.
        If the amount of data between startTime and endTime is greater than limit, return the data in the case of startTime + limit.

        :param symbol: The symbol you want to get the funding rate for
        :param start_time: The start time of the data you want to query
        :param end_time: The end time of the data you want to query
        :param limit: The number of results to return, maximum 1000

        https://bingx-api.github.io/docs/swapV2/market-api.html#_6-funding-rate-history
        """

        endpoint = "/openApi/swap/v2/quote/fundingRate"
        payload = {"symbol": symbol.upper(), "limit": limit} if start_time is None or end_time is None else {"symbol": symbol.upper(), "startTime": start_time, "endTime": end_time, "limit": limit}

        response = self.get(endpoint, payload)
        return response.json()

    def get_k_line_data(self, symbol: str, interval: str, start_time: int | None = None, end_time: int | None = None, limit: int = 500) -> dict[str, Any]:
        """
        Get the latest Kline Data.
        If startTime and endTime are not sent, the latest k-line data will be returned by default

        :param symbol: The trading pair you want to get the Kline data for
        :param interval: The interval of the Kline data, possible values: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 1w, 1M
        :param start_time: The start time of the Kline data, in milliseconds
        :param end_time: The end time of the Kline data, in milliseconds
        :param limit: The number of Kline data to return, maximum 1440

        https://bingx-api.github.io/docs/swapV2/market-api.html#_7-k-line-data
        """

        endpoint = "/openApi/swap/v2/quote/klines"
        payload = {"symbol": symbol.upper(), "interval": interval, "limit": limit} if start_time is None or end_time is None else {"symbol": symbol.upper(), "interval": interval, "startTime": start_time, "endTime": end_time, "limit": limit}

        response = self.get(endpoint, payload)
        return response.json()

    def get_swap_open_positions(self, symbol: str) -> dict[str, Any]:
        """
        It returns the open positions for a given symbol.

        :param symbol: The symbol you want to get the open interest for

        https://bingx-api.github.io/docs/swapV2/market-api.html#_8-get-swap-open-positions
        """

        endpoint = "/openApi/swap/v2/quote/openInterest"
        payload = {"symbol": symbol.upper()}

        response = self.get(endpoint, payload)
        return response.json()

    def get_ticker(self, symbol: str | None = None) -> dict[str, Any]:
        """
        It returns the ticker for a given symbol.
        If no transaction pair parameters are sent, all transaction pair information will be returned

        :param symbol: The symbol you want to get the ticker for. If you don't specify a symbol, you'll getthe ticker for all symbols

        https://bingx-api.github.io/docs/swapV2/market-api.html#_9-get-ticker
        """

        endpoint = "/openApi/swap/v2/quote/ticker"
        payload = {} if symbol is None else {"symbol": symbol.upper()}

        response = self.get(endpoint, payload)
        return response.json()
