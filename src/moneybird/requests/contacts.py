from typing import ClassVar, Type

from moneybird.requests import BaseRequestModel
from moneybird.responses.contacts import ContactList


class ContactListRequest(BaseRequestModel[ContactList]):
    method: ClassVar[str] = "GET"
    url: ClassVar[str] = "{administration_id}/contacts.json"

    administration_id: str
    response_model: ClassVar[Type[ContactList]] = ContactList
