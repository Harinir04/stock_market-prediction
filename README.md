# 💹 Stock Market Prediction App (with Sentiment Analysis)

### 🚀 Overview
This futuristic **Stock Market Prediction Web App** predicts the **next 7 days of stock prices** using **Machine Learning (Linear Regression)**.  
It supports both **Live Data (Yahoo Finance)** and **Offline CSV Dataset**, with an elegant **Dark Mode UI** and simulated **Market Sentiment Analysis**.

---

## 🧠 Features
✅ Predict next 7-day stock closing prices using Linear Regression  
✅ Fetch **live stock data** directly from **Yahoo Finance**  
✅ Use **offline CSV dataset** as a backup  
✅ Display **interactive charts** for stock trends and predictions  
✅ **Simulated Sentiment Analysis** for visualizing market mood  
✅ Download predicted data as a **CSV file**  
✅ Fully **responsive dark mode** with glowing animations and large fonts  

---

## 🧩 Tech Stack
| Component | Technology Used |
|------------|----------------|
| **Frontend / UI** | Streamlit (Dark Mode with Custom CSS) |
| **Backend / ML Model** | Scikit-learn (Linear Regression) |
| **Data Source** | Yahoo Finance API (`yfinance` package) |
| **Data Visualization** | Matplotlib, Streamlit Charts |
| **Language** | Python 3.10+ |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/stock-market-prediction-app.git
cd stock-market-prediction-app
```

### 2️⃣ Install required dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ (Optional) Add backup dataset
Place your `backup_stock_data.csv` in the project folder if you want to test offline mode.

### 4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📂 File Structure
```
📁 Stock-Market-Prediction-App
 ├── app.py                     # Main Streamlit App
 ├── backup_stock_data.csv      # Offline dataset (optional)
 ├── requirements.txt           # Dependencies
 └── README.md                  # Documentation
```

---

## 📊 Example Output
- **Data Source:** Yahoo Finance  
- **Predicted 7-day prices** displayed in a clean table  
- **Market sentiment pie chart** showing Positive, Neutral, Negative distribution  
- **Actual vs Predicted** stock price bar chart  
- **Download option** for CSV of predictions  

---

## 🧮 Machine Learning Model
The model uses **Linear Regression** from `sklearn` to predict stock closing prices based on past data.  
It converts date values into numerical form (ordinal) for regression fitting.

---

## 🧠 Simulated Sentiment Analysis
Since live sentiment APIs are not used here, random values simulate market mood.  
This gives a realistic view of how market sentiment can affect predictions visually.

---

## ⚠️ Challenges
- Real-time data availability and missing values  
- Overfitting on short-term trends  
- Lack of true sentiment data (simulated here)  
- API rate limits when fetching multiple stocks  

---

## 💡 Future Enhancements
- Integrate **real sentiment analysis** using Twitter or News API  
- Add **deep learning models (LSTM / GRU)** for better accuracy  
- Include **technical indicators** (RSI, MACD, Bollinger Bands)  
- Add **portfolio tracking and recommendations**

---

## 🏆 Credits
Developed by **[Your Name] (2025)**  
Built with ❤️ using **Python + Streamlit**

---

## 📸 Preview
![Dark Mode Screenshot](preview.png)

---

## 🧾 License
This project is open-source and free to use for educational purposes.

