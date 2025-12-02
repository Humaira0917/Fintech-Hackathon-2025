from fastapi import APIRouter
from ml_model.predict import fraud_predict

router = APIRouter()

@router.post("/")
def fraud_check(data: dict):
    score = fraud_predict(data)
    return {"fraud_risk": score}