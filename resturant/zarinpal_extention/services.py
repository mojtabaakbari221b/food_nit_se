from typing import Dict

from django.urls import reverse
from zeep import Client

from django_zarinpal.config import (
    ZARINPAL_START_GATEWAY,
    ZARINPAL_SANDBOX, ZARINPAL_VERIFY_TRANSACTION_VIEW)
from django_zarinpal.config import (
    ZARINPAL_WEBSERVICE,
    ZARINPAL_MERCHANT_ID
)
from django_zarinpal.exceptions import (
    CouldNotStartTransaction,
    AmountIsLessThanMinimum
)
from django_zarinpal.models import Transaction


def start_transaction(request, transaction_data: Dict) -> str:
    transaction = Transaction(
        user=transaction_data["user"],
        amount=transaction_data["amount"],
        description=transaction_data["description"],
        is_test=ZARINPAL_SANDBOX
    )

    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(
        ZARINPAL_MERCHANT_ID,
        transaction_data["amount"],
        transaction_data["description"],
        transaction_data["email"],
        transaction_data["mobile"],
        request.build_absolute_uri(reverse(ZARINPAL_VERIFY_TRANSACTION_VIEW))
    )

    if result.Status == 100:
        transaction.authority = result.Authority
        transaction.save()
        return ZARINPAL_START_GATEWAY + result.Authority
    elif result.Status == -3:
        raise AmountIsLessThanMinimum(
            f"response:{result}, transaction data: {transaction_data}")
    else:
        raise CouldNotStartTransaction(
            f"response:{result}, transaction data: {transaction_data}")
