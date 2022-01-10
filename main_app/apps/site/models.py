import uuid
from typing import Optional, List

from pydantic import UUID4, BaseModel, Field

from database.main_db import db_provider


class SomeModelName(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    info: Optional[str]

    class Config:
        allow_population_by_field_name = True

class Stock(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    title: Optional[str] = ""
    description: Optional[str] = ""
    imgsrc: Optional[list] = []
    slug: str
    display_order: int = 0

    def insert_db(self):
        db_provider.stocks_db.insert_one(
            self.dict(by_alias = True)
        )

    class Config:
        allow_population_by_field_name = True

class StaffMember(BaseModel):
    name: str = ""
    scope: str = ""
    imgsrc: List[str] = []
    working_yeasrs: str = ""

class RequestCall(BaseModel):
    name: str
    phone: str
