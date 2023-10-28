from typing import ClassVar, Type

from requestmodel import RequestModel, ResponseType

from moneybird.responses import AdministrationList


class BaseRequestModel(RequestModel[ResponseType]):
    """Always use this as base class for your request models.
    This way we can override settings easily."""


class AdministrationRequest(BaseRequestModel[AdministrationList]):
    method: ClassVar[str] = "GET"
    url: ClassVar[str] = "administrations"

    response_model: ClassVar[Type[AdministrationList]] = AdministrationList
