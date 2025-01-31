from fastapi import FastAPI
from api.check_imei import router as imei_router

app = FastAPI()

app.include_router(imei_router)

@app.get("/")
def home():
    return {"message": "Welcome to IMEI Checker API"}