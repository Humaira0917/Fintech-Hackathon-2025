import os
import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Paths
ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model.pkl"
VECT_PATH = ROOT / "vectorizer.pkl"

# -------------------------------
# TRAINING DATA
# -------------------------------
spam_sms = [
    "URGENT! Your account has been suspended. Verify here: http://fakebank.example/verify",
    "Congratulations! You've won a $1000 gift card. Click here to claim.",
    "Your OTP is 482903. Do not share with anyone.",
    "Final notice: unpaid bill. Pay immediately: http://pay.example",
    "Bank alert: unauthorized login attempt. Verify now.",
]

safe_sms = [
    "Hey, are we meeting at 5 today?",
    "Your appointment is scheduled for tomorrow.",
    "Please review the attached document.",
    "Your package has been delivered.",
    "Happy birthday! Have a great day."
]

df = pd.DataFrame({
    "text": spam_sms + safe_sms,
    "label": ["spam"] * len(spam_sms) + ["safe"] * len(safe_sms)
})

# Shuffle
df = df.sample(frac=1).reset_index(drop=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2)

# Vectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
X_test_vec = vectorizer.transform(X_test)
pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# Save files
joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECT_PATH)

print("Saved model:", MODEL_PATH)
print("Saved vectorizer:", VECT_PATH)
