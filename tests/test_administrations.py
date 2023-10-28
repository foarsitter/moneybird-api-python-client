from moneybird.client import get_client
from moneybird.requests import AdministrationRequest


def test_administrations() -> None:
    client = get_client()
    request = AdministrationRequest()

    response = request.send(client)

    assert len(response) == 1
