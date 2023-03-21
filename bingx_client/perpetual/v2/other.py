from typing import Any

from bingx_client._exceptions import ServerError
from bingx_client._http_manager import _HTTPManager


class Other(_HTTPManager):
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__http_manager = _HTTPManager(api_key, secret_key)

    def generate_listen_key(self) -> dict[str, Any]:
        """
        Generates a listen key valid for 1 hour

        https://bingx-api.github.io/docs/swapV2/other-interface.html#generate-listen-key
        """

        endpoint =  "/openApi/user/auth/userDataStream"

        response = self.__http_manager.post(endpoint)
        return response.json()

    def extend_listen_key_validity_period(self, listen_key: str) -> int:
        """
        The validity period is extended to 60 minutes after this call, and it is recommended to send a ping every 30 minutes.

        200 - success, 204 - not content, 404 - not find key

        return: 200 if the listen key is extended successfully

        https://bingx-api.github.io/docs/swapV2/other-interface.html#extend-listen-key-validity-period
        """

        endpoint = "/openApi/user/auth/userDataStream"
        payload = {"listenKey": listen_key}

        try:
            response = self.__http_manager.put(endpoint, payload)
        except ServerError as e:
            return e.error_code
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

        try:
            response = self.__http_manager.delete(endpoint, payload)
        except ServerError as e:
            return e.error_code
        return response.status_code