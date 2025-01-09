from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)

@app.get("/predict")
@limiter.limit("5/minute")
async def predict_risk(request: Request):
    return {"message": "Your prediction request was successful."}
