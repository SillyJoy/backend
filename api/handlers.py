from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.collections import thermal_insulators_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")
id = 0


@router.get("/")
def get_catalog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="feed.html",
        context={"insulator": thermal_insulators_db[id], "liked": len(thermal_insulators_db[id]["likes"])}
    )


@router.get("/add")
def get_catalog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add.html",
        context={"insulator": thermal_insulators_db[id], "liked": len(thermal_insulators_db[id]["likes"])}
    )


@router.get("/list")
def get_catalog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="list.html",
        context={"db": thermal_insulators_db, "liked": len(thermal_insulators_db[id]["likes"])}
    )
