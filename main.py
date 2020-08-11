from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from loader import app
import api
app.mount("/static", StaticFiles(directory="webapp/static"), name="static")

#templates = Jinja2Templates(directory="templates") 
frontend = Jinja2Templates(directory="webapp/templates/frontend") 

@app.get("/")
async def home_page(request: Request):
	return frontend.TemplateResponse('index.html', {"request": request})
