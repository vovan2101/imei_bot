from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.imei_validator import is_valid_imei
from services.imei_check import check_imei_info
from config import API_TOKEN


router = APIRouter(prefix="/api", tags=["IMEI"])


class IMEIRequest(BaseModel):
    imei: str
    token: str


@router.post("/check-imei")
async def check_imei(request: IMEIRequest):
    # Проверяем токен
    if request.token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    # Проверяем IMEI на валидность
    if not is_valid_imei(request.imei):
        raise HTTPException(status_code=400, detail="Invalid IMEI format")
    
    # Запрашиваем данные из imeicheck.net
    imei_data = check_imei_info(request.imei)


    if imei_data is None:
        raise HTTPException(status_code=500, detail="IMEI check service error")
    
    return imei_data