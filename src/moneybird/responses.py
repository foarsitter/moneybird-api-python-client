from typing import List

from pydantic import BaseModel, RootModel


class MoneyBirdBaseModel(BaseModel):
    pass


class Administration(MoneyBirdBaseModel):
    id: int
    name: str
    language: str
    currency: str
    country: str
    time_zone: str
    access: str


class AdministrationList(RootModel[List[Administration]]):
    root: List[Administration]

    def __len__(self) -> int:
        return len(self.root)
