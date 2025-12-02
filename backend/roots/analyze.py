from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def analyze_data(data: dict):
    return {"message": "Analyze Endpoint Working", "input": data}