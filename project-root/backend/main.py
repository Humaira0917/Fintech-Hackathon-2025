from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.sms_route import router as sms_router

app = FastAPI(title="SMS Phishing Detector API")

# Allow frontend (any origin during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sms_router)

# Run using:
# uvicorn backend.main:app --reload
