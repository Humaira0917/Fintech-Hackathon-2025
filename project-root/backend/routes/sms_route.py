from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from pathlib import Path
import sys

# FIX → Add ml_model folder to import path
BASE_DIR = Path(__file__).resolve().parents[1]  # backend/
ML_DIR = BASE_DIR / "ml_model"
sys.path.append(str(ML_DIR))

from predict_sms import predict_text  # Now Python can find it

router = APIRouter()

class SMSRequest(BaseModel):
    text: str

@router.post("/sms/detect")
def detect_sms(payload: SMSRequest) -> Dict:
    result = predict_text(payload.text)
    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"],
    }
