from typing import Any

from bingx_client._http_manager import _HTTPManager
from bingx_client.spot._types import (
    HistoryDeposit,
    HistoryTransfer,
    HistoryWithdraw,
    UniversalTransfer,
)


class Transfer:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def universal_transfer(self, transfer: UniversalTransfer) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/spot/user-interface.html#user-universal-transfer
        """

        endpoint = "/openApi/api/v3/asset/transfer"
        payload = transfer.to_dict()

        response = self.__http_manager.post(endpoint, payload)
        return response.json()

    def get_universal_transfer_history(self, history_transfer: HistoryTransfer) -> dict[str, Any]:
        """

        https://bingx-api.github.io/docs/spot/user-interface.html#query-user-universal-transfer-history-user-data
        """

        endpoint = "/openApi/api/v3/asset/transfer"
        payload = history_transfer.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()

    def get_deposit_history(self, deposit_history: HistoryDeposit) -> list[dict[str, Any]]:
        """

        https://bingx-api.github.io/docs/spot/user-interface.html#deposit-history-supporting-network
        """

        endpoint = "/openApi/api/v3/capital/deposit/hisrec"
        payload = deposit_history.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()

    def get_withdraw_history(self, withdraw_history: HistoryWithdraw) -> list[dict[str, Any]]:
        """

        https://bingx-api.github.io/docs/spot/user-interface.html#withdraw-history-supporting-network
        """

        endpoint = "/openApi/api/v3/capital/withdraw/history"
        payload = withdraw_history.to_dict()

        response = self.__http_manager.get(endpoint, payload)
        return response.json()
