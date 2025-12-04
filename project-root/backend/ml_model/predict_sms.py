import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
model = joblib.load(ROOT / "model.pkl")
vectorizer = joblib.load(ROOT / "vectorizer.pkl")

def predict_text(text: str):
    X = vectorizer.transform([text])
    probas = model.predict_proba(X)[0]
    pred = model.predict(X)[0]
    
    conf = probas[list(model.classes_).index(pred)] * 100
    return {"prediction": pred, "confidence": round(conf, 2)}
