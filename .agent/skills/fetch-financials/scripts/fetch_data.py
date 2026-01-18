import sys
import json
import requests
import os

def fetch_alpha_vantage(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    
    # Endpoints needed for Buffett, Lynch, and Dalio metrics
    functions = ["OVERVIEW", "INCOME_STATEMENT", "BALANCE_SHEET", "GLOBAL_QUOTE"]
    master_data = {"symbol": symbol}

    for func in functions:
        params = {
            "function": func,
            "symbol": symbol,
            "apikey": api_key
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Merge into master object based on function type
            if func == "OVERVIEW":
                master_data["overview"] = data
            elif func == "GLOBAL_QUOTE":
                master_data["quote"] = data.get("Global Quote", {})
            else:
                # We only need the most recent annual report for analysis
                master_data[func.lower()] = data.get("annualReports", [{}])[0]
                
        except Exception as e:
            master_data[f"error_{func}"] = str(e)

    return master_data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No ticker symbol provided"}))
        sys.exit(1)
        
    ticker = sys.argv[1].upper()
    # Antigravity automatically handles your environment variables
    key = os.getenv("ALPHA_VANTAGE_API_KEY") 
    
    if not key:
        print(json.dumps({"error": "API Key missing in environment"}))
        sys.exit(1)

    result = fetch_alpha_vantage(ticker, key)
    print(json.dumps(result, indent=2))