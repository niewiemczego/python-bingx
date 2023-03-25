
import os

import pytest
from dotenv import load_dotenv

from bingX.exceptions import ClientError
from bingX.spot.transfer import Transfer
from bingX.spot.types import (
    HistoryDeposit,
    HistoryTransfer,
    HistoryWithdraw,
    TransferType,
    UniversalTransfer,
)

load_dotenv()

class TestTransfer:
    @pytest.fixture
    def transfer(self) -> Transfer:
        api_key = os.getenv('API_KEY')
        secret_key = os.getenv('SECRET_KEY')
        return Transfer(api_key, secret_key)

    def test_universal_transfer_valid_type(self, transfer: Transfer):
        response = transfer.universal_transfer(UniversalTransfer(TransferType.FUND_PFUTURES))
        assert isinstance(response, dict)

    def test_universal_transfer_invalid_type(self, transfer: Transfer):
        with pytest.raises(AttributeError):
            transfer.universal_transfer(UniversalTransfer(TransferType.INVALID))

    def test_get_universal_transfer_history_valid_type(self, transfer: Transfer):
        response = transfer.get_universal_transfer_history(HistoryTransfer(TransferType.FUND_PFUTURES))
        assert isinstance(response, dict)

    def test_get_universal_transfer_history_invalid_type(self, transfer: Transfer):
        with pytest.raises(AttributeError):
            transfer.get_universal_transfer_history(HistoryTransfer(TransferType.INVALID))

    def test_deposit_history_valid(self, transfer: Transfer):
        response = transfer.get_deposit_history(HistoryDeposit())
        assert isinstance(response, list)

    def test_withdraw_history_valid(self, transfer: Transfer):
        response = transfer.get_withdraw_history(HistoryWithdraw())
        assert isinstance(response, list)