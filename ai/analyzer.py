import pandas as pd 
import requests
from dotenv import load_dotenv 
import os 

load_dotenv()

def fetch_stock_data(symbol):
    url = f"http://localhost:5000/api/stock/{symbol}"