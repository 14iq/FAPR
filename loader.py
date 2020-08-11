from fastapi import FastAPI

from config import openapi_url, docs_url, redoc_url
#loader.py - to load instances

app = FastAPI(openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url)