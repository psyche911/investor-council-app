from typing import Dict, Any, List
import os
from .council import Buffett, Lynch, Dalio, Munger

def generate_report(ticker: str, financials: Dict[str, Any], prices: Dict[str, Any], output_dir: str = "analyses") -> str:
    """
    Orchestrates the council analysis and generates a consolidated Markdown report.
    """
    
    # Initialize Council
    council = [Buffett(), Lynch(), Dalio(), Munger()]
    
    report = f"# Investor Council Report: {ticker}\n\n"
    
    # Financial Summary Section
    report += "## Financial Snapshot\n"
    # Add price summary if available
    if "Time Series (Daily)" in prices:
        latest_date = sorted(prices["Time Series (Daily)"].keys())[-1]
        latest_close = prices["Time Series (Daily)"][latest_date]["4. close"]
        report += f"- **Latest Close ({latest_date}):** ${float(latest_close):.2f}\n"

    report += "\n---\n\n"
    
    # Council Opinions
    report += "## Council Opinions\n\n"
    
    for member in council:
        try:
            member_report = member.analyze(ticker, financials)
            report += member_report + "\n\n---\n\n"
        except Exception as e:
            report += f"### Error analyzing with {type(member).__name__}\n"
            report += f"> {str(e)}\n\n---\n\n"

    # Save Report
    ticker_dir = os.path.join(output_dir, ticker)
    os.makedirs(ticker_dir, exist_ok=True)
    report_path = os.path.join(ticker_dir, "report.md")
    
    with open(report_path, "w") as f:
        f.write(report)
        
    return report_path
