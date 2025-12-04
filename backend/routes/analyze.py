from fastapi import APIRouter # pyright: ignore[reportMissingImports]

router = APIRouter()

@router.post("/")
def analyze_data(data: dict):
    return {"message": "Analyze Endpoint Working", "input": data}