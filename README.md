🧠 Decision Regret Checker

An AI-powered web application that estimates the likelihood of regretting a decision using personality traits based on the Big Five psychological model.

📌 Project Overview

Decision-making is often influenced by personality traits.
This project applies machine learning to estimate regret tendency based on the Big Five Personality Model.

The system:

Processes personality trait scores

Uses a trained classification model

Predicts regret probability

Provides personalized advice

Adjusts risk based on decision type

This project demonstrates a complete machine learning workflow:
Data processing → Feature engineering → Model training → Deployment

🧠 Psychological Foundation

The model is based on the Big Five Personality Model, originally developed by personality researchers such as Lewis Goldberg.

The five traits used:

Neuroticism – Emotional stability and stress tendency

Conscientiousness – Discipline and responsibility

Extraversion – Social energy

Agreeableness – Cooperation and empathy

Openness – Curiosity and creativity

Research suggests certain personality traits correlate with higher regret and overthinking tendencies.

⚙ How It Works

Users rate themselves on five personality dimensions (1–5 scale).

The trained machine learning model predicts regret probability.

Decision type (career, financial, relationship, etc.) adjusts risk.

The app provides structured advice based on prediction level.

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

📊 Machine Learning Pipeline

Data Cleaning

Feature Engineering (Trait Score Aggregation)

Synthetic Label Construction

Train/Test Split

Cross Validation

Model Selection (Random Forest / Gradient Boosting)

Performance Evaluation

Deployment

📈 Model Performance

Accuracy: ~95% (on synthetic label)

Cross-validation applied for stability

Feature importance validated against psychological expectations

Note: High accuracy is expected due to formula-based label construction.

🚀 Features

Interactive web interface

Personality-based prediction

Decision-type risk adjustment

Personalized advice generation

Fully deployed cloud application

📂 Project Structure

decision-regret-checker/

│

├── app.py

├── regret_model.pkl

├── requirements.txt

└── README.md

▶ Run Locally

pip install -r requirements.txt

streamlit run app.py

⚠ Disclaimer

This tool estimates behavioral tendencies based on personality modeling and machine learning.

Author

Pooja Maru
