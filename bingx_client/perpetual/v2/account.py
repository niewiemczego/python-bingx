from typing import Any

from bingx_client._http_manager import _HTTPManager
from bingx_client.perpetual.v2._types import ProfitLossFundFlow


class Account(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def get_details(self, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Get asset information of user's Perpetual Account

        https://bingx-api.github.io/docs/swapV2/account-api.html#_1-get-perpetual-swap-account-asset-information
        """

        endpoint = "/openApi/swap/v2/user/balance"
        payload = {} if recvWindow is None else {"recvWindow": recvWindow}

        response = self.get(endpoint, payload)
        return response.json()

    def get_swap_positions(self, symbol: str | None = None, recvWindow: int | None = None) -> dict[str, Any]:
        """
        Retrieve information on users' positions of Perpetual Swap.

        https://bingx-api.github.io/docs/swapV2/account-api.html#_2-perpetual-swap-positions
        """

        endpoint = "/openApi/swap/v2/user/positions"
        if symbol is None:
            payload = {} if recvWindow is None else {"recvWindow": recvWindow}
        else:
            payload = {"symbol": symbol.upper()} if recvWindow is None else {"symbol": symbol.upper(), "recvWindow": recvWindow}

        response = self.get(endpoint, payload)
        return response.json()

    def get_profit_loss_fund_flow(self, profit_loss_fund_flow: ProfitLossFundFlow | None = None) -> dict[str, Any]:
        """
        Query the capital flow of the perpetual contract under the current account.
        If neither startTime nor endTime is sent, only the data of the last 7 days will be returned.
        If the incomeType is not sent, return all types of account profit and loss fund flow.
        Only keep the last 3 months data.

        https://bingx-api.github.io/docs/swapV2/account-api.html#_3-get-account-profit-and-loss-fund-flow
        """
        endpoint = "/openApi/swap/v2/user/income"
        payload = {} if profit_loss_fund_flow is None else profit_loss_fund_flow.to_dict()

        response = self.get(endpoint, payload)
        return response.json()
