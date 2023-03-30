from typing import Any

from bingX._http_manager import _HTTPManager


class Account:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def get_details(self, currency: str) -> dict[str, Any]:
        """
        Get asset information of user's Perpetual Account

        https://bingx-api.github.io/docs/swap/account-api.html#_1-get-perpetual-swap-account-asset-information
        """

        endpoint = "/api/v1/user/getBalance"
        payload = {"currency": currency.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]

    def get_swap_positions(self, symbol: str) -> dict[str, Any]:
        """
        Retrieve information on users' positions of Perpetual Swap.

        https://bingx-api.github.io/docs/swap/account-api.html#_2-perpetual-swap-positions
        """

        endpoint = "/api/v1/user/getPositions"
        payload = {"symbol": symbol.upper()}

        response = self.__http_manager.post(endpoint, payload)
        return response.json()["data"]