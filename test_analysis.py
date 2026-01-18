from backend.analysis.report import generate_report
import os
import shutil

def test_analysis():
    # Mock Data
    ticker = "MOCK_TECH"
    
    financials = {
        "income_statement": {
            "annualReports": [
                {"netIncome": "1000000000", "fiscalDateEnding": "2023-12-31"}
            ]
        },
        "balance_sheet": {
            "annualReports": [
                {"totalShareholderEquity": "5000000000", "totalLiabilities": "2000000000"}
            ]
        },
        "cash_flow": {},
        "overview": {
            "PEGRatio": "0.8",
            "QuarterlyEarningsGrowthYOY": "0.25",
            "PERatio": "20"
        }
    }
    
    prices = {
        "Time Series (Daily)": {
            "2023-12-31": {"4. close": "150.00"}
        }
    }
    
    print("Running Analysis Test...")
    try:
        report_path = generate_report(ticker, financials, prices, output_dir="test_analyses")
        print(f"✅ Report generated at: {report_path}")
        
        with open(report_path, "r") as f:
            content = f.read()
            
        # Verify Key Logic
        print("\nVerifying Report Content:")
        
        # Buffett Check
        if "$ROIC" in content and "Pass" in content: # 1B/7B = 14% -> Fail actually. 
             # Wait, 1/7 is 14.2%. My mock data gives 14.2%. 
             pass
             
        if "Calculated ROIC: **14.29%**" in content:
            print("- ✅ Buffett ROIC Calculation correct.")
        elif "Calculated ROIC" in content:
             print(f"- ⚠️ Buffett ROIC present but value unexpected based on mock data.")
        else:
             print("- ❌ Buffett analysis missing or broken.")

        # Lynch Check
        if "Fast Grower" in content:
            print("- ✅ Lynch categorization correct (Fast Grower > 20%).")
        else:
            print("- ❌ Lynch categorization failed.")

        # Munger Check
        if "Munger Score" in content:
             print("- ✅ Munger Score present.")
        else:
             print("- ❌ Munger Score missing.")

        # Cleanup
        # shutil.rmtree("test_analyses") 
        # print("\nTest artifacts cleaned up.")

    except Exception as e:
        print(f"❌ Analysis failed: {e}")

if __name__ == "__main__":
    test_analysis()
