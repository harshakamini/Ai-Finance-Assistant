
# app.py - Streamlit Personal Finance Assistant

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import datetime

st.set_page_config(page_title="Personal Finance Assistant", layout="wide")
st.title("💸 Personal Finance Assistant - AI Powered")

# Load Models
@st.cache_resource
def load_models():
    classifier, vectorizer = joblib.load("classifier.pkl")
    budget_model = joblib.load("budget_model.pkl")
    forecast_model = joblib.load("forecast_model.pkl")
    return classifier, vectorizer, budget_model, forecast_model

classifier, vectorizer, budget_model, forecast_model = load_models()

# File upload
uploaded_file = st.file_uploader("Upload your transactions CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Data")
    st.dataframe(df.head())

    # ----------- Expense Categorization -----------
    st.subheader("📌 Step 1: Expense Categorization")
    desc_vec = vectorizer.transform(df['Description'])
    df['Predicted Category'] = classifier.predict(desc_vec)
    st.write(df[['Description', 'Predicted Category']])

    # ----------- Budget Recommendation -----------
    st.subheader("📈 Step 2: Budget Recommendation")
    df['desc_len'] = df['Description'].apply(len)
    features = pd.get_dummies(df[['Predicted Category', 'desc_len']])

    # Match columns to model
    model_features = budget_model.feature_names_in_
    for col in model_features:
        if col not in features:
            features[col] = 0
    features = features[model_features]

    df['Predicted Amount'] = budget_model.predict(features)
    st.write(df[['Description', 'Predicted Category', 'Predicted Amount']])

    # ----------- Expense Forecasting -----------
    st.subheader("🔮 Step 3: Expense Forecasting")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    monthly = df.resample('M', on='Date').sum()['Amount']

    forecast = forecast_model.forecast(steps=6)

    # Plot
    fig, ax = plt.subplots()
    monthly.plot(ax=ax, label="Past Monthly Total")
    forecast.plot(ax=ax, label="Forecast (Next 6 months)", color='green')
    ax.legend()
    st.pyplot(fig)

    # ----------- Download Categorized Data -----------
    st.subheader("⬇️ Download Categorized & Predicted Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results as CSV", csv, "categorized_predictions.csv", "text/csv")
