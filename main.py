import argparse
import sys
import os
from dotenv import load_dotenv
from backend.data.fetcher import AlphaVantageClient
from backend.analysis.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="Investor Council Analysis Tool")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol (e.g., IBM, AAPL)")
    args = parser.parse_args()
    
    ticker = args.ticker.upper()
    print(f"🚀 Starting analysis for {ticker}...")
    
    # 1. Environment Setup
    load_dotenv()
    if not os.getenv("ALPHA_VANTAGE_API_KEY"):
        print("❌ Error: ALPHA_VANTAGE_API_KEY not found in .env")
        sys.exit(1)
        
    # 2. Fetch Data
    print("📡 Fetching financial data from Alpha Vantage...")
    try:
        client = AlphaVantageClient()
        financials = client.get_financials(ticker)
        prices = client.get_price_data(ticker)
        print("✅ Data fetched successfully.")
    except Exception as e:
        print(f"❌ Failed to fetch data: {e}")
        sys.exit(1)
        
    # 3. Analyze & Generate Report
    print("🧠 Council is deliberating...")
    try:
        # Save to the 'analyses' directory in the project root
        output_dir = os.path.join(os.getcwd(), "analyses")
        report_path = generate_report(ticker, financials, prices, output_dir=output_dir)
        print(f"✅ Analysis complete! Report saved to:\n   {report_path}")
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
