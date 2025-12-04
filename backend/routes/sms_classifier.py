from fastapi import APIRouter # pyright: ignore[reportMissingImports]
from ml_model.predict import sms_predict

router = APIRouter()

@router.post("/")
def classify_sms(text: str):
    result = sms_predict(text)
    return {"prediction": result}