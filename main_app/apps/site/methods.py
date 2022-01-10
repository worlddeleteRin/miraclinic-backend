from .models import Stock, StaffMember, Slider
from database.main_db import db_provider
from typing import List

def get_stocks_db():
    stocks_dict = db_provider.stocks_db.find({})
    if not stocks_dict:
        return []
    stocks = [Stock(**stock).dict() for stock in stocks_dict]
    return stocks

def get_staff_members_db():
    staff_members_raw = db_provider.staff_members_db.find({})
    staff_members = [StaffMember(**member).dict() for member in staff_members_raw]
    return staff_members

def get_main_sliders() -> List[Slider]:
    main_sliders_raw = db_provider.sliders_db.find(
        {}
    ).sort('display_order', 1)
    main_sliders = [Slider(**slider) for slider in main_sliders_raw]
    return main_sliders
