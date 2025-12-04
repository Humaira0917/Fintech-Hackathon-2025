from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from routes.analyze import router as AnalyzeRouter
from routes.sms_classifier import router as SMSRouter
from routes.fraud_detection import router as FraudRouter

app = FastAPI(title="FinTech Hackathon API")

@app.get("/")
def home():
    return {"status": "FinTech API Running"}

app.include_router(AnalyzeRouter, prefix="/analyze")
app.include_router(SMSRouter, prefix="/sms")
app.include_router(FraudRouter, prefix="/fraud")