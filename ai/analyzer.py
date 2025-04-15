import pandas as pd 
import requests
from dotenv import load_dotenv 
import os 

load_dotenv()

def fetch_stock_data(symbol):
    url = f"http://localhost:5000/api/stock/{symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def analyze_stock(symbol, historical_data):
    df = pd.DataFrame(historical_data)
    df["short_ma"] = df["close"].rolling(window=5).mean()
    df["long_ma"] = df["close"].rolling(window=20).mean()

    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else None

    signal = None

    if prev is not None and latest["short_ma"] > latest["long_ma"] and prev["short_ma"] < prev["long_ma"]:
        signal = "buy"
    elif prev is not None and latest["short_ma"] < latest["long_ma"] and prev["short_ma"] > prev["long_ma"]:
        signal = "sell"

    return {
        "symbol": symbol,
        "signal": signal,
         "price" : latest["close"],
         "error": None
        }
    

if __name__ == "__main__": 

    mock_data = [
        {"close" : 150 + i * 0.5 , 
   "timestamp": f"2025-04-{10+i}"} for i in range(30)
    ]
    result = analyze_stock("AAPL", mock_data)
    print(result) 