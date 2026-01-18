import os
import requests
import logging
import time
from typing import Dict, Any, Optional

class AlphaVantageClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Set ALPHA_VANTAGE_API_KEY environment variable.")
        self.base_url = "https://www.alphavantage.co/query"
        self.logger = logging.getLogger(__name__)

    def _get_data(self, function: str, symbol: str) -> Dict[str, Any]:
        """Helper to make API requests."""
        # Alpha Vantage Free Tier Limit: 5 calls per minute. 
        # We need a significant delay to be safe if making sequential calls.
        time.sleep(12) 
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Check for API errors
            if "Error Message" in data:
                self.logger.error(f"Alpha Vantage Error for {symbol}: {data['Error Message']}")
                raise ValueError(f"Alpha Vantage API Error: {data['Error Message']}")
            if "Information" in data:
                 self.logger.warning(f"Alpha Vantage Info for {symbol}: {data['Information']}")
            
            return data
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error fetching data for {symbol}: {e}")
            raise

    def get_financials(self, symbol: str) -> Dict[str, Any]:
        """Fetches Income Statement, Balance Sheet, and Cash Flow."""
        financials = {}
        try:
            financials["income_statement"] = self._get_data("INCOME_STATEMENT", symbol)
            financials["balance_sheet"] = self._get_data("BALANCE_SHEET", symbol)
            financials["cash_flow"] = self._get_data("CASH_FLOW", symbol)
            # Company Overview is essential for sector, industry, PE, PEG, etc.
            financials["overview"] = self._get_data("OVERVIEW", symbol) 
        except Exception as e:
             self.logger.error(f"Failed to fetch financials for {symbol}: {e}")
             raise
        
        return financials

    def get_price_data(self, symbol: str) -> Dict[str, Any]:
        """Fetches Daily Time Series (Free endpoint)."""
        return self._get_data("TIME_SERIES_DAILY", symbol)
