from enum import Enum

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from config import openapi_url, docs_url, redoc_url


app = FastAPI(openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url)
app.mount("/static", StaticFiles(directory="webapp/static"), name="static")

#templates = Jinja2Templates(directory="templates") 
frontend = Jinja2Templates(directory="webapp/templates/frontend") 

@app.get("/")
async def home_page(request: Request):
	return frontend.TemplateResponse('index.html', {"request": request})
