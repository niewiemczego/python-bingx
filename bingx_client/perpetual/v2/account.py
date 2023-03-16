from typing import Any

from bingx_client._http_manager import _HTTPManager
from bingx_client.perpetual.v2.types import ProfitLossFundFlow


class Account(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def get_details(self, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Get asset information of user's Perpetual Account
        """

        endpoint = "/openApi/swap/v2/user/balance"
        payload = {} if recvWindow is None else {"recvWindow": recvWindow}

        response = self._get(endpoint, payload)
        return response.json()

    def get_swap_positions(self, symbol: str | None = None, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Retrieve information on users' positions of Perpetual Swap.
        """

        endpoint = "/openApi/swap/v2/user/positions"
        if symbol is None:
            payload = {} if recvWindow is None else {"recvWindow": recvWindow}
        else:
            payload = {"symbol": symbol} if recvWindow is None else {"symbol": symbol, "recvWindow": recvWindow}

        response = self._get(endpoint, payload)
        return response.json()

    def get_profit_loss_fund_flow(self, profit_loss_fund_flow: ProfitLossFundFlow):
        """
        Query the capital flow of the perpetual contract under the current account.
        """
        endpoint = "/openApi/swap/v2/user/income"
        payload = profit_loss_fund_flow.to_dict()

        response = self._get(endpoint, payload)
        return response.json()
