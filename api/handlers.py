from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.collections import insulators_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_catalog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="feed.html",
        context={"hotels": insulators_db}
    )


@router.get("/hotel/{hotel_id}")
def get_hotel_detail(request: Request, hotel_id: int):
    hotel = next((h for h in insulators_db if h["id"] == hotel_id), None)

    return templates.TemplateResponse(
        request=request,
        name="hotel.html",
        context={"hotel": hotel}
    )