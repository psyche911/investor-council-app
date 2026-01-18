import pandas as pd
from typing import Dict, Any, Optional

def get_latest_value(data: Dict[str, Any], key: str, report_type: str = "annualReports") -> float:
    """Helper to safely extract the latest value from Alpha Vantage financial reports."""
    try:
        reports = data.get(report_type, [])
        if not reports:
            return 0.0
        val = reports[0].get(key, "0")
        return float(val) if val and val != "None" else 0.0
    except (ValueError, IndexError, TypeError):
        return 0.0

def calculate_roic(income_statement: Dict[str, Any], balance_sheet: Dict[str, Any]) -> float:
    """
    Return on Invested Capital (ROIC).
    Formula: NOPAT / (Total Equity + Total Debt - Cash)
    Approximation: Net Income / (Total Shareholder Equity + Total Liabilities)
    """
    net_income = get_latest_value(income_statement, "netIncome")
    equity = get_latest_value(balance_sheet, "totalShareholderEquity")
    liabilities = get_latest_value(balance_sheet, "totalLiabilities")
    
    invested_capital = equity + liabilities
    if invested_capital == 0:
        return 0.0
    
    return net_income / invested_capital

def calculate_debt_to_equity(balance_sheet: Dict[str, Any]) -> float:
    """
    Debt to Equity Ratio.
    Formula: Total Liabilities / Total Shareholder Equity
    """
    liabilities = get_latest_value(balance_sheet, "totalLiabilities")
    equity = get_latest_value(balance_sheet, "totalShareholderEquity")
    
    if equity == 0:
        return float('inf')
    
    return liabilities / equity

def calculate_peg(overview: Dict[str, Any]) -> float:
    """
    PEG Ratio (Price/Earnings to Growth).
    Alpha Vantage 'OVERVIEW' endpoint provides this directly usually.
    If not, we'd need historical growth rates which are complex to compute from just one report.
    """
    try:
        peg = overview.get("PEGRatio", "0")
        return float(peg) if peg and peg != "None" else 0.0
    except (ValueError, TypeError):
        return 0.0

def get_pe_ratio(overview: Dict[str, Any]) -> float:
    try:
        pe = overview.get("PERatio", "0")
        return float(pe) if pe and pe != "None" else 0.0
    except (ValueError, TypeError):
        return 0.0

def get_earnings_growth(overview: Dict[str, Any]) -> float:
    """
    Quarterly Earnings Growth YOY.
    """
    try:
        growth = overview.get("QuarterlyEarningsGrowthYOY", "0")
        return float(growth) if growth and growth != "None" else 0.0
    except (ValueError, TypeError):
        return 0.0
