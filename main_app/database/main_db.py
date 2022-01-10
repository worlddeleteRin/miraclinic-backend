# from fastapi import FastAPI from functools import lru_cache
from functools import lru_cache

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from config import settings

from pydantic import BaseModel


class DbProvider(BaseModel):
    db_client: MongoClient
    db_main: Database 

    some_db: Collection
    services_pages_db: Collection
    stocks_db: Collection
    staff_members_db: Collection
    services_db: Collection
    categories_db: Collection
    sliders_db: Collection

    class Config:
        arbitrary_types_allowed = True


@lru_cache
def setup_db_main() -> DbProvider:
    print('call setup db_main function')
    db_client  = MongoClient(settings.DB_URL)
    db_main = db_client[settings.DB_NAME]
    db_provider = DbProvider(
                db_client = db_client,
                db_main = db_main,
                some_db = db_main["db_name"], 
                services_pages_db = db_main["services-pages"],
                stocks_db = db_main["stocks"],
                staff_members_db = db_main["staff_members"],
                services_db = db_main["services"],
                categories_db = db_main["categories"],
                sliders_db = db_main["sliders"],
            )
    return db_provider

db_provider = setup_db_main()

