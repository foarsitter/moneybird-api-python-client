from moneybird.client import get_client
from moneybird.requests import contacts


def test_contact_list_request() -> None:
    client = get_client()
    request = contacts.ContactListRequest(administration_id="253628522405299379")

    response = request.send(client)

    assert len(response) == 50
