hide_docs = False

openapi_url = "/openapi.json"
docs_url = "/docs"
redoc_url = "/redoc"

if hide_docs:
    openapi_url = None
    docs_url = None
    redoc_url = None