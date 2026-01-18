# Fetch Financials Skill

**Description:** Use this skill when the user asks for financial data, investment analysis, or a "council review" of a specific stock ticker.

## Goal
Fetches comprehensive real-time and fundamental data from Alpha Vantage for multi-agent financial reasoning.

## Instructions
1. Extract the ticker symbol from the user's prompt.
2. Verify if the `ALPHA_VANTAGE_API_KEY` exists in the environment.
3. Execute the python script: `python scripts/fetch_data.py <TICKER>`
4. Pass the resulting JSON output to the next agent in the chain (e.g., the Council Agents).

## Constraints
- Do not make more than 5 calls per minute (Free Tier limit).
- Always return the raw JSON to the model context for analysis; do not summarize unless asked.