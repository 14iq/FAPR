hide_docs = False

openapi_url = "/api/openapi.json"
docs_url = "/api/docs"
redoc_url = "/api/redoc"

if hide_docs:
    openapi_url = None
    docs_url = None
    redoc_url = None