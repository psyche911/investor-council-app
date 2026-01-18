from abc import ABC, abstractmethod
from typing import Dict, Any, List
from .metrics import calculate_roic, calculate_debt_to_equity, calculate_peg, get_pe_ratio, get_earnings_growth

class CouncilMember(ABC):
    @abstractmethod
    def analyze(self, ticker: str, financials: Dict[str, Any]) -> str:
        pass

class Buffett(CouncilMember):
    def analyze(self, ticker: str, financials: Dict[str, Any]) -> str:
        income = financials.get("income_statement", {})
        balance = financials.get("balance_sheet", {})
        
        roic = calculate_roic(income, balance)
        de_ratio = calculate_debt_to_equity(balance)
        
        report = f"### Warren Buffett Analysis\n\n"
        
        # MOAT Analysis (ROIC)
        report += f"**Moat Check (ROIC):** \n"
        report += f"Formula: $ROIC = \\frac{{Net Income}}{{Equity + Liabilities}}$\n\n"
        report += f"Calculated ROIC: **{roic:.2%}**\n"
        if roic > 0.15:
            report += "- ✅ **Pass:** ROIC > 15%. Indicates a durable competitive advantage.\n"
        else:
            report += "- ❌ **Fail:** ROIC < 15%. This business may qualify as a commodity.\n"
            
        # Balance Sheet (Debt)
        report += f"\n**Financial Strength (Debt/Equity):** \n"
        report += f"Formula: $D/E = \\frac{{Total Liabilities}}{{Shareholder Equity}}$\n\n"
        report += f"Calculated D/E: **{de_ratio:.2f}**\n"
        if de_ratio < 0.5:
             report += "- ✅ **Pass:** Conservative debt usage.\n"
        else:
             report += "- ⚠️ **Caution:** Debt levels are getting high.\n"
             
        return report

class Lynch(CouncilMember):
    def analyze(self, ticker: str, financials: Dict[str, Any]) -> str:
        overview = financials.get("overview", {})
        
        peg = calculate_peg(overview)
        growth = get_earnings_growth(overview)
        
        report = f"### Peter Lynch Analysis\n\n"
        
        # Categorization
        report += f"**Categorization:**\n"
        if growth > 0.20:
            category = "Fast Grower"
            report += f"- This is a **{category}** (Growth > 20%).\n"
        elif 0.10 <= growth <= 0.20:
            category = "Stalwart"
            report += f"- This is a **{category}** (Growth 10-20%).\n"
        else:
            category = "Slow Grower"
            report += f"- This is a **{category}** (Growth < 10%).\n"
            
        # Valuation (PEG)
        report += f"\n**Valuation Check (PEG):** \n"
        report += f"Formula: $PEG = \\frac{{P/E Ratio}}{{Earnings Growth Rate}}$\n\n"
        report += f"Calculated PEG: **{peg:.2f}**\n"
        
        if peg < 1.0:
            report += "- ✅ **Undervalued:** PEG < 1.0. Potential bargain.\n"
        elif 1.0 <= peg <= 2.0:
             report += "- ⚖️ **Fair Value:** PEG between 1.0 and 2.0.\n"
        else:
             report += "- ❌ **Overvalued:** PEG > 2.0. Pricey for the growth offered.\n"
             
        return report

class Dalio(CouncilMember):
    def analyze(self, ticker: str, financials: Dict[str, Any]) -> str:
        # Placeholder for Macro analysis
        report = f"### Ray Dalio Analysis\n\n"
        report += "> *\"Cash is trash, but timing is everything.\"*\n\n"
        
        report += "**Macro Perspective:**\n"
        report += "- **Inflation Hedge:** [Requires Manual Context]. Does this company have pricing power?\n"
        report += "- **Debt Cycle:** Check if the industry is highly leveraged in a rising rate environment.\n"
        report += "- **Diversification:** Ensure this asset is uncorrelated with your existing portfolio.\n"
        
        return report

class Munger(CouncilMember):
    def analyze(self, ticker: str, financials: Dict[str, Any]) -> str:
        income = financials.get("income_statement", {})
        balance = financials.get("balance_sheet", {})
        overview = financials.get("overview", {})
        
        roic = calculate_roic(income, balance)
        growth = get_earnings_growth(overview)
        de_ratio = calculate_debt_to_equity(balance)
        
        report = f"### Charlie Munger Analysis\n\n"
        report += "**The Lollapalooza Effect:**\n"
        
        score = 0
        triggers = []
        
        # 1. Economic Scale (High ROIC)
        if roic > 0.15:
            score += 2
            triggers.append("Economic Scale (High ROIC)")
            
        # 2. Growth (Pricing power proxy)
        if growth > 0.15:
            score += 2
            triggers.append("Growth/Pricing Power")
            
        # 3. Financial Fortitude (Low Debt) - Inversion
        if de_ratio < 0.5:
             score += 2
             triggers.append("Financial Reliability")
        else:
             # Inversion penalty
             score -= 2
             triggers.append("High Debt Penalty (Inverted)")
             
        # Synergy Bonus
        if len([t for t in triggers if "Penalty" not in t]) >= 2:
            score += 2
            triggers.append("Synergy Bonus")
            
        # Cap score at 10, min 0
        score = max(0, min(10, score))
        
        report += f"**Munger Score:** {score}/10\n\n"
        report += "**Identified Mental Models:**\n"
        for t in triggers:
            symbol = "❌" if "Penalty" in t else "✅"
            report += f"- {symbol} {t}\n"
            
        return report
