from __future__ import annotations
import uuid
from typing import Optional, List

from pydantic import UUID4, BaseModel, Field

from database.main_db import db_provider

from pymongo.collection import ReturnDocument

# from .utils import find_category_by_slug



class SomeModelName(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    info: Optional[str]

    class Config:
        allow_population_by_field_name = True

class Category(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    slug: str
    label: str = ""
    name: str
    imgsrc: List[str] = []
    view_rating: int = 1
    description: str = ""

    @staticmethod
    def remove_all():
        db_provider.categories_db.remove()

    @staticmethod
    def get_category_by_id(
        category_id: UUID4,
    ) -> Category | None:
        categoryRaw = db_provider.categories_db.find_one(
            {"_id": category_id}
        )
        if not categoryRaw:
            return None
        return Category(**categoryRaw)

    @staticmethod
    def find_category_by_slug(
        category_slug: str,
    ) -> Category | None:
        categoryRaw = db_provider.categories_db.find_one(
            {"slug": category_slug}
        )
        if not categoryRaw:
            return None
        return Category(**categoryRaw)

    def return_if_exists(self, responseObject: dict):
        if isinstance(responseObject, Service):
            return Category(**responseObject)
        return None

    def insert_db(self):
        db_provider.categories_db.insert_one(
            self.dict(by_alias=True)
        )

    def update_db(self):
        updated_service = db_provider.categories_db.find_one_and_update( 
            {"_id": self.id},
            self.dict(by_alias=True),
            return_document=ReturnDocument.AFTER
        )
        self.return_if_exists(updated_service)

    def delete_db(self):
        db_provider.categories_db.find_one_and_delete(
            {"_id": self.id}
        )

    class Config:
        allow_population_by_field_name = True

class Service(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    price: str
    categories_id: List[UUID4] = []
    categories_slug: List[str] = []

    @staticmethod
    def remove_all():
        db_provider.services_db.remove()

    def return_if_exists(self, responseObject: dict):
        if isinstance(responseObject, Service):
            return Service(**responseObject)
        return None

    def insert_db(self):
        self.find_assign_category()
        db_provider.services_db.insert_one(
            self.dict(by_alias=True)
        )

    def update_db(self):
        updated_service = db_provider.services_db.find_one_and_update( 
            {"_id": self.id},
            self.dict(by_alias=True),
            return_document=ReturnDocument.AFTER
        )
        self.return_if_exists(updated_service)

    def delete_db(self):
        db_provider.services_db.find_one_and_delete(
            {"_id": self.id}
        )

    def find_assign_category(self): 
        self.categories_id = []
        for category_slug in self.categories_slug:
            category: Category | None = Category.find_category_by_slug(category_slug)
            if isinstance(category, Category):
                self.categories_id.append(category.id)


