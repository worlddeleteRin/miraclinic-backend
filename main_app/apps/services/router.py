from fastapi import APIRouter
from typing import List, Optional

from config import settings

from database.main_db import db_provider
from pydantic import UUID4

from apps.site.content import header_links, main_slider
# from .methods import get_stocks_db, get_staff_members_db
from .models import Category, Service
from .utils import get_categories, get_services

router = APIRouter(
    prefix = "/services",
    tags = ["services"],
)

@router.get("/categories")
def get_categories_request(
) -> List[Category]:
    categories: List[Category] = get_categories(
    )
    return categories

@router.get("/categories/{categoryId}")
def get_category(
    categoryId: UUID4,
) -> Optional[Category]:
    category = Category.get_category_by_id(categoryId)
    return category 

@router.get("/")
def get_services_request(
    page: int = 1,
    limit: int = 50,
    category_id: Optional[UUID4] = None,
):
    assert page > 0
    assert limit > 0
    assert limit <= 100
    services: List[Service] = get_services(
        limit = limit,
        page = page,
        category_id = category_id,
    )
    return services 
     
