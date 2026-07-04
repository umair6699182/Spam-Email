📧 Spam Email Detector

A machine learning web application that detects whether an email message is **Spam** or **Not Spam** using Natural Language Processing and a trained classification model.

🚀 Features

- Detects spam emails from user input
- Shows prediction result: Spam or Not Spam
- Displays model confidence score
- Simple Streamlit web interface
- Uses saved ML model and TF-IDF vectorizer

🛠️ Tech Stack

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Machine Learning Classification Model
- Streamlit
- Joblib

📁 Project Structure

spam-email-detector/
│
├── app/
│   └── app.py
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── predict.py
│   └── train.py
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── requirements.txt
├── README.md
└── spam_detector.ipynb
