from .models import Stock, StaffMember
from database.main_db import db_provider

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
