import os, requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={api_key}"

response = requests.get(url).json()
print("Success!" if "Global Quote" in response else f"Error: {response}")