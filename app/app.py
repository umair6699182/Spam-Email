import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.predict import predict_email

# Page configuration
st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Spam Email Detector")
st.write(
    "Paste an email message below and check whether it is Spam or Not Spam."
)

# Input area
email = st.text_area(
    "Paste Email",
    height=200,
    placeholder="Enter email content here..."
)

# Prediction button
if st.button("Predict"):

    if email.strip() == "":
        st.warning("⚠️ Please enter an email message first.")

    else:
        label, confidence = predict_email(email)

        if label == "Spam":
            st.error("🚨 This email is Spam")
        else:
            st.success("✅ This email is Not Spam")

        st.metric(
            label="Model Confidence",
            value=f"{confidence:.2f}%"
        )

        st.progress(confidence / 100)