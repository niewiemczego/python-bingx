from typing import Any

from bingx_client._http_manager import _HTTPManager
from bingx_client.perpetual.v2.types import MarginType, Order, PositionSide


class Other(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def generate_listen_key(self) -> dict[str, Any]:
        """
        Generates a listen key valid for 1 hour

        https://bingx-api.github.io/docs/swapV2/other-interface.html#generate-listen-key
        """

        endpoint =  "/openApi/user/auth/userDataStream"

        response = self._post(endpoint)
        return response.status_code

    def extend_listen_key_validity_period(self, listen_key: str) -> int:
        """
        The validity period is extended to 60 minutes after this call, and it is recommended to send a ping every 30 minutes.

        200 - success, 204 - not content, 404 - not find key

        return: 200 if the listen key is extended successfully

        https://bingx-api.github.io/docs/swapV2/other-interface.html#extend-listen-key-validity-period
        """

        endpoint = "/openApi/user/auth/userDataStream"
        payload = {"listenKey": listen_key}

        response = self._put(endpoint, payload)
        return response.status_code

    def delete_listen_key(self, listen_key: str) -> int:
        """
        Delete User data flow.

        200 - success, 204 - not content, 404 - not find key

        return: 200 if the listen key is deleted successfully

        https://bingx-api.github.io/docs/swapV2/other-interface.html#delete-listen-key
        """

        endpoint = "/openApi/user/auth/userDataStream"
        payload = {"listenKey": listen_key}

        response = self._delete(endpoint, payload)
        return response.status_code