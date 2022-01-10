from fastapi import APIRouter
from fastapi.background import BackgroundTasks

from config import settings

from database.main_db import db_provider

from apps.site.content import header_links, main_slider
from apps.notifications.mail import send_mail_background
from .methods import get_stocks_db, get_staff_members_db
from .models import RequestCall

router = APIRouter(
    prefix = "/site",
    tags = ["site"],
)

@router.get("/common-info")
def get_common_info():
    common_info = {
        "logo_src": settings.base_static_url + "logo_black.jpg",
        "phone": "+8000000000",
        "phone_display": "8 (000) 000 00 00",
        "working_time": "Пн — Вс: 9:00 — 19:00",
        "location": {
            "address_name": "г. Ялта, Гаспра, Севастопольское шоссе, 12",
            "map_link": "https://yandex.ru/map-widget/v1/?um=constructor%3Ac947c29ff6662e1e8c0adbc94cdb9ac435c1f26a7c6b6a2a9c1b361ffa2d5ece&amp;source=constructor",
        },
        "socials": {
            "instagram": {
                "link": "https://www.instagram.com/miraclinic_crimea/",
                "icon": "ant-design:instagram-filled",
                "color": "#833AB4",
            },
            "vk": {
                "link": "https://vk.com/miraclinic_crimea/",
                "icon": "akar-icons:vk-fill",
                "color": "#4C75A3",
            },
            "whatsapp": {
                "link": "https://whatsapp.com",
                "icon": "fontisto:whatsapp",
                "color": "green",
            },
            "viber": { 
                "link": "https://viber.com",
                "icon": "fa-brands:viber",
                "color": "#59267c",
            }
        }

    }
    return common_info 

@router.get("/header-links")
def get_header_links():
    return header_links


@router.get("/stocks")
def get_stocks():
    return get_stocks_db()

@router.get("/main-slider")
def get_main_slider():
    return main_slider

@router.get("/staff-members")
def get_staff_members():
    return get_staff_members_db()

@router.post("/request-call")
def request_call(
    call_info: RequestCall,
    background_tasks: BackgroundTasks,
):
    print(f"call info is {call_info.dict()}")
    message_body = {
        "phone": call_info.phone,
        "name": call_info.name,
    }
    send_mail_background(
        subject="Miraclinic. Запрос на обратный звонок",
        background_tasks=background_tasks,    
        # email_to="worlddelete0@yandex.ru",
        # email_to="fast.code.main@gmail.com",
        email_to="e.gusea@gmail.com",
        body=message_body,
    )
    return {
        "status": "success"
    }

