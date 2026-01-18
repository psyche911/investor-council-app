import os
from dotenv import load_dotenv
from backend.data.fetcher import AlphaVantageClient
import json

def test_fetcher():
    load_dotenv()
    client = AlphaVantageClient()
    symbol = "IBM"
    
    print(f"Testing fetcher for {symbol}...")
    
    try:
        # Test 1: Financials
        print("\nFetching Financials...")
        financials = client.get_financials(symbol)
        expected_keys = ["income_statement", "balance_sheet", "cash_flow", "overview"]
        if all(k in financials for k in expected_keys):
            print("✅ Financials structure valid.")
        else:
            print(f"❌ Missing keys in financials: {set(expected_keys) - set(financials.keys())}")

        # Test 2: Price Data
        print("\nFetching Price Data...")
        prices = client.get_price_data(symbol)
        if "Time Series (Daily)" in prices:
            print("✅ Price data valid.")
        else:
            print(f"❌ Price data missing Time Series info: {prices.keys()}")

    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    test_fetcher()
