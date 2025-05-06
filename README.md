# 💸 AI Personal Finance Assistant

An AI-powered web application that helps users automatically *categorize expenses, **recommend budgets, and **forecast future spending* using uploaded transaction data. Built with *Streamlit*, this app simplifies personal finance management through machine learning and time-series forecasting.

---

## 🚀 Features

- 📂 *CSV Upload* – Upload your transaction history (CSV format).
- 🧠 *Expense Categorization* – Uses a Random Forest classifier to label transaction categories.
- 📊 *Budget Recommendation* – Suggests budget allocations using linear regression.
- 🔮 *Expense Forecasting* – Predicts expenses for the next 6 months using ARIMA time-series modeling.
- ⬇ *Download Results* – Export the processed, categorized data as CSV.

---

## 🧰 Tech Stack

- *Frontend*: Streamlit
- *Backend & ML*: Python, scikit-learn, statsmodels, pandas
- *Visualization*: Matplotlib
- *Model Persistence*: joblib
- *Environment*: Python 3.10+

---

## 🏗 Folder Structure



bash
finance_chatbot_app/
│
├── app.py                  # Streamlit main app
├── chatbot_utils.py        # Utility functions (model loading)
├── .env                    # Environment file (optional)
├── models/
│   ├── classifier.pkl       # Expense categorization model
│   ├── budget_model.pkl     # Budget prediction model
│   ├── forecast_model.pkl   # Forecasting model
│   └── vectorizer.pkl       # TF-IDF Vectorizer
├── sample_data.csv         # Example CSV file
└── README.md



---

## 📷 Screenshots

| Upload CSV | Categorized Transactions | Forecast Graph |
|------------|--------------------------|----------------|
| ![Upload](screenshots/upload.png) | ![Categorized](screenshots/categories.png) | ![Forecast](screenshots/forecast.png) |

---

## 🧪 How to Run Locally

1. *Clone the repository*
   ```bash
   git clone https://github.com/your-username/finance-chatbot-app.git
   cd finance-chatbot-app


Create a virtual environment :

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


RUN THE APP:

streamlit run app.py


📁 Sample CSV Format

Date,Description,Amount
2024-10-01,Amazon Purchase,300
2024-10-03,Uber Ride,120
2024-10-05,Electricity Bill,2200
...


🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---
Let me know your GitHub username or repo name if you'd like me to tailor it further!
