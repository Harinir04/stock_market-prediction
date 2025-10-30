# ---------------- STOCK MARKET PREDICTION APP (PREMIUM DARK MODE - LARGE TEXT) ----------------
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.linear_model import LinearRegression
import nltk
import datetime as dt
import random
import matplotlib.pyplot as plt
from io import BytesIO
import os

# ---------------- INITIAL SETUP ----------------
nltk.download('punkt', quiet=True)
st.set_page_config(page_title="💹 Stock Market Prediction", layout="wide")

# ---------------- CUSTOM DARK THEME ----------------
st.markdown("""
    <style>
        /* Background and Text */
        .stApp {
            background-color: #0A0A0A;
            color: #FFFFFF;
            font-family: 'Poppins', sans-serif;
            font-size: 20px; 
        }

        /* Main Title */
        .main-title {
            text-align: center;
            color: #00BFFF;
            font-size: 52px;  
            font-weight: bold;
            text-shadow: 0px 0px 20px #00BFFF;
            margin-bottom: 0.3em;
            animation: glow 2s infinite alternate;
        }

        /* Sub Title */
        .sub-title {
            text-align: center;
            color: #CCCCCC;
            font-size: 24px; 
            margin-bottom: 30px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #00BFFF;
            color: white;
            font-size: 22px; 
            border-radius: 14px;
            height: 3.3em;
            width: 100%;
            border: none;
            box-shadow: 0px 0px 12px #00BFFF;
            transition: all 0.3s ease-in-out;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #0099CC;
            box-shadow: 0px 0px 25px #00FFFF;
            transform: scale(1.07);
        }

        /* Radio & Select labels */
        .stRadio label, .stSelectbox label {
            font-size: 22px; 
            color: #FFFFFF;
            font-weight: 600;
        }

        /* Selectbox input */
        div[data-baseweb="select"] > div {
            font-size: 20px !important;
            color: #000000 !important;
        }

        /* Table and Dataframe */
        .stDataFrame, .stTable {
            background-color: #111111;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0,191,255,0.4);
        }

        /* Divider line */
        hr {
            border: 1px solid #00BFFF;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #AAAAAA;
            font-size: 18px; 
            margin-top: 70px;
        }

        /* Glow Animation */
        @keyframes glow {
            0% {text-shadow: 0 0 10px #00BFFF, 0 0 20px #00FFFF;}
            50% {text-shadow: 0 0 25px #00FFFF, 0 0 45px #00BFFF;}
            100% {text-shadow: 0 0 10px #00BFFF, 0 0 20px #00FFFF;}
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 class="main-title">📊 Stock Market Prediction with Sentiment Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Predict the Next 7-Day Stock Prices using Live or Offline Data</p>', unsafe_allow_html=True)
st.write("---")

# ---------------- ABOUT SECTION ----------------
with st.expander("📘 About this Project"):
    st.write("""
    This futuristic app predicts *next 7-day stock prices* using *Machine Learning (Linear Regression)*.

    🚀 Features:
    - *Yahoo Finance (Live Data)* – Fetches the latest online stock data  
    - *Preloaded CSV Dataset* – Uses offline backup data for quick analysis  
    - *Simulated Sentiment Analysis* – Visualizes the market's mood  
    """)

# ---------------- USER INPUT ----------------
data_source = st.radio("Choose Data Source:", ["📡 Yahoo Finance (Live Data)", "📂 Preloaded CSV Dataset"])

# ✅ Stock Ticker List (with full forms)
ticker_dict = {
    "AAPL": "Apple Inc.",
    "TSLA": "Tesla Inc.",
    "INFY.NS": "Infosys Ltd.",
    "TCS.NS": "Tata Consultancy Services Ltd.",
    "RELIANCE.NS": "Reliance Industries Ltd.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc. (Google)",
    "AMZN": "Amazon.com Inc.",
    "HDFCBANK.NS": "HDFC Bank Ltd.",
    "SBIN.NS": "State Bank of India"
}

ticker_display_list = [f"{k} ({v})" for k, v in ticker_dict.items()]

selected_display = st.selectbox(
    "🔍 Search or Select a Stock (with Full Name):",
    options=ticker_display_list,
    index=None,
    placeholder="Type or choose a stock ticker..."
)

ticker = selected_display.split(" ")[0] if selected_display else None

# ---------------- PREDICTION LOGIC ----------------
if st.button("🔮 Predict"):
    if not ticker:
        st.warning("⚠️ Please select a stock to continue.")
    else:
        st.info("Fetching and processing data... ⏳")
        try:
            # ---------------- FETCH DATA ----------------
            if data_source == "📡 Yahoo Finance (Live Data)":
                start = dt.datetime.now() - dt.timedelta(days=365)
                end = dt.datetime.now()
                data = yf.download(ticker, start=start, end=end)
                if data.empty:
                    st.error("❌ No data found for this ticker.")
                    st.stop()
            else:
                csv_file = "backup_stock_data.csv"
                if not os.path.exists(csv_file):
                    st.error(f"❌ File not found: {csv_file}")
                    st.stop()
                data = pd.read_csv(csv_file)
                data["Date"] = pd.to_datetime(data["Date"])
                data.set_index("Date", inplace=True)

                if "Ticker" in data.columns:
                    filtered = data[data["Ticker"].str.upper() == ticker.upper()]
                    if filtered.empty:
                        st.error(f"❌ No data found for '{ticker}' in CSV.")
                        st.stop()
                    data = filtered

            # ---------------- DISPLAY DATA ----------------
            st.success(f"✅ Data Source Used: {data_source}")
            st.subheader("📊 Recent Stock Data")
            st.dataframe(data.tail())

            # ---------------- TRAIN MODEL ----------------
            data["DateNum"] = data.index.map(dt.datetime.toordinal)
            X = np.array(data["DateNum"]).reshape(-1, 1)
            y = np.array(data["Close"])
            model = LinearRegression().fit(X, y)

            # ---------------- PREDICT FUTURE ----------------
            end_date = data.index[-1]
            future_dates = [end_date + dt.timedelta(days=i) for i in range(1, 8)]
            future_dates_num = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
            predictions = model.predict(future_dates_num).flatten()

            forecast_df = pd.DataFrame({
                "Date": [d.strftime("%Y-%m-%d") for d in future_dates],
                "Predicted Close Price": np.round(predictions, 2)
            })

            st.subheader("📅 Predicted Prices for Next 7 Days")
            st.table(forecast_df)

            # ---------------- DOWNLOAD BUTTON ----------------
            csv_buffer = BytesIO()
            forecast_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download Predictions (CSV)",
                data=csv_buffer.getvalue(),
                file_name=f"{ticker}_predictions.csv",
                mime="text/csv"
            )

            # ---------------- SENTIMENT SIMULATION ----------------
            st.subheader("💬 Market Sentiment (Simulated)")
            pos = random.randint(40, 70)
            neg = random.randint(10, 40)
            neu = max(0, 100 - (pos + neg))
            sentiments = ['Positive', 'Neutral', 'Negative']
            values = [pos, neu, neg]
            avg_sentiment = (pos - neg) / 100

            if avg_sentiment > 0.2:
                st.success("Overall Sentiment: Positive 😊")
            elif avg_sentiment < -0.2:
                st.error("Overall Sentiment: Negative 😟")
            else:
                st.info("Overall Sentiment: Neutral 😐")

            fig, ax = plt.subplots(facecolor="#0A0A0A")
            colors = ["#00FF99", "#00BFFF", "#FF5555"]
            wedges, texts, autotexts = ax.pie(
                values, labels=sentiments, autopct='%1.1f%%', startangle=90,
                textprops={'color': "white", 'fontsize': 16}, colors=colors
            )
            for w in wedges:
                w.set_edgecolor("#0A0A0A")
            ax.axis('equal')
            st.pyplot(fig)

            # ---------------- CHARTS ----------------
            if len(data) >= 7:
                st.subheader("📈 Actual vs Predicted Price Comparison")
                combined_df = pd.concat(
                    [data.tail(7)["Close"].reset_index(drop=True), forecast_df["Predicted Close Price"]], axis=1)
                combined_df.columns = ["Actual Price", "Predicted Price"]
                st.bar_chart(combined_df)

            st.subheader("📉 Stock Price Chart (Full Data)")
            st.line_chart(data["Close"])

        except Exception as e:
            st.error(f"❌ Error: {e}")

# ---------------- FOOTER ----------------
st.write("---")
st.markdown('<p class="footer">⚡ Developed by <b>Harini R</b> | Stock Market Prediction Project 2025 💻</p>', unsafe_allow_html=True)
