from loader import app

@app.get("/api")
async def test_api():
    return {"hello": 9}