# stock_market-prediction
#ðŸ’¹ Stock Market Prediction App (with Sentiment Analysis)

### ðŸš€ Overview
This futuristic **Stock Market Prediction Web App** predicts the **next 7 days of stock prices** using **Machine Learning (Linear Regression)**.  
It supports both **Live Data (Yahoo Finance)** and **Offline CSV Dataset**, with an elegant **Dark Mode UI** and simulated **Market Sentiment Analysis**.

---

## ðŸ§  Features
âœ… Predict next 7-day stock closing prices using Linear Regression  
âœ… Fetch **live stock data** directly from **Yahoo Finance**  
âœ… Use **offline CSV dataset** as a backup  
âœ… Display **interactive charts** for stock trends and predictions  
âœ… **Simulated Sentiment Analysis** for visualizing market mood  
âœ… Download predicted data as a **CSV file**  
âœ… Fully **responsive dark mode** with glowing animations and large fonts  

---

## ðŸ§© Tech Stack
| Component | Technology Used |
|------------|----------------|
| **Frontend / UI** | Streamlit (Dark Mode with Custom CSS) |
| **Backend / ML Model** | Scikit-learn (Linear Regression) |
| **Data Source** | Yahoo Finance API (`yfinance` package) |
| **Data Visualization** | Matplotlib, Streamlit Charts |
| **Language** | Python 3.10+ |

---

## âš™ï¸ Installation & Setup

### 1ï¸âƒ£ Clone this repository
```bash
git clone https://github.com/your-username/stock-market-prediction-app.git
cd stock-market-prediction-app
```

### 2ï¸âƒ£ Install required dependencies
```bash
pip install -r requirements.txt
```

### 3ï¸âƒ£ (Optional) Add backup dataset
Place your `backup_stock_data.csv` in the project folder if you want to test offline mode.

### 4ï¸âƒ£ Run the Streamlit app
```bash
streamlit run app.py
```

---

## ðŸ“‚ File Structure
```
ðŸ“ Stock-Market-Prediction-App
 â”œâ”€â”€ app.py                     # Main Streamlit App
 â”œâ”€â”€ backup_stock_data.csv      # Offline dataset (optional)
 â”œâ”€â”€ requirements.txt           # Dependencies
 â””â”€â”€ README.md                  # Documentation
```

---

## ðŸ“Š Example Output
- **Data Source:** Yahoo Finance  
- **Predicted 7-day prices** displayed in a clean table  
- **Market sentiment pie chart** showing Positive, Neutral, Negative distribution  
- **Actual vs Predicted** stock price bar chart  
- **Download option** for CSV of predictions  

---

## ðŸ§® Machine Learning Model
The model uses **Linear Regression** from `sklearn` to predict stock closing prices based on past data.  
It converts date values into numerical form (ordinal) for regression fitting.

---

## ðŸ§  Simulated Sentiment Analysis
Since live sentiment APIs are not used here, random values simulate market mood.  
This gives a realistic view of how market sentiment can affect predictions visually.

---

## âš ï¸ Challenges
- Real-time data availability and missing values  
- Overfitting on short-term trends  
- Lack of true sentiment data (simulated here)  
- API rate limits when fetching multiple stocks  

---

## ðŸ’¡ Future Enhancements
- Integrate **real sentiment analysis** using Twitter or News API  
- Add **deep learning models (LSTM / GRU)** for better accuracy  
- Include **technical indicators** (RSI, MACD, Bollinger Bands)  
- Add **portfolio tracking and recommendations**

---

## ðŸ† Credits
Developed by **[Your Name] (2025)**  
Built with â¤ï¸ using **Python + Streamlit**

---

## ðŸ“¸ Preview
![Dark Mode Screenshot](preview.png)

---

## ðŸ§¾ License
This project is open-source and free to use for educational purposes.