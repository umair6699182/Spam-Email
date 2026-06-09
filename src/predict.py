import joblib
from pathlib import Path
from src.preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "spam_model.pkl")
vectorizer = joblib.load(BASE_DIR / "models" / "vectorizer.pkl")


def predict_email(message):
    cleaned = clean_text(message)
    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]

    confidence = max(probabilities) * 100

    if prediction == 1:
        label = "Spam"
    else:
        label = "Not Spam"

    return label, confidence


if __name__ == "__main__":
    email = input("Enter email text: ")
    label, confidence = predict_email(email)

    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.2f}%")