from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.collections import thermal_insulators_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_catalog(request: Request, id: int = 0, next: str = "false"):
    nextid = id + 1
    if next == "true":
        id += 1
        nextid = id + 1
    if id < 0 or id > len(thermal_insulators_db):
        id = 0
        nextid = 1
    if nextid > len(thermal_insulators_db):
        nextid = 0
    return templates.TemplateResponse(
        request=request,
        name="feed.html",
        context={"insulator": thermal_insulators_db[id], "liked": len(thermal_insulators_db[id]["likes"]), "nextid": nextid}
    )


@router.get("/add")
def get_catalog(request: Request):
    for i in thermal_insulators_db:
        if i["status"] == 2:
            id = i["id"]
            break
    return templates.TemplateResponse(
        request=request,
        name="add.html",
        context={"insulator": thermal_insulators_db[id]}
    )


@router.get("/list")
def get_catalog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="list.html",
        context={"db": thermal_insulators_db}
    )
