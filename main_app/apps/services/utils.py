from typing import List, Optional
from database.main_db import db_provider
from .models import Category, Service
from pydantic import UUID4


def get_categories() -> List[Category]:
    categoriesRaw = db_provider.categories_db.find(
        {}
    )
    categories: List[Category] = [Category(**category) for category in categoriesRaw]
    return categories

def get_services(
    page: int,
    limit: int,
    category_id: Optional[UUID4] = None,
) -> List[Service]:
    filters: dict = {}
    if category_id:
        filters["categories_id"] = category_id
    skip_count = (limit * (page - 1))
    servicesRaw = db_provider.services_db.find(
        filters
        # filters
    ).skip(skip_count).limit(limit)
    services: List[Service] = [Service(**service) for service in servicesRaw]
    return services 
