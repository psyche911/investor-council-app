# Investor Council App

**Use the wisdom of legends to analyze the market.**

The **Investor Council** is an AI-powered financial analysis tool that fetches real-time market data and evaluates it through the distinct mental models of four legendary investors: **Warren Buffett**, **Peter Lynch**, **Charlie Munger**, and **Ray Dalio**.

![Dashboard Preview](https://placehold.co/600x400/18181b/fbbf24?text=Investor+Council+App)

## 🚀 Features

-   **Multi-Persona Analysis**:
    -   **Buffett**: Focuses on ROIC (>15%) and Debt/Equity ratios (<0.5).
    -   **Lynch**: Categorizes stocks (Fast Grower, Stalwart) and checks PEG ratios.
    -   **Munger**: Scores companies (1-10) based on "Lollapalooza" effects (Moals + Prices).
    -   **Dalio**: Provides a macro-risk framework (Inflation, Debt Cycles).
-   **Automated Data Fetching**: Retrieves Income Statements, Balance Sheets, and Cash Flows via **Alpha Vantage**.
-   **Premium Dashboard**: A Next.js 14 application with dark mode and LaTeX formula rendering for financial math.

## 🛠 Tech Stack

-   **Backend**: Python 3.11, Pandas, Alpha Vantage API.
-   **Frontend**: Next.js 14, Tailwind CSS, React Markdown, KaTeX.
-   **Data Source**: Alpha Vantage (Free Tier compatible with rate limiting).

## 📋 Prerequisites

-   Python 3.11+
-   Node.js 18+
-   [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key) (Free)

## ⚙️ Setup

### 1. Clone & Configure
```bash
git clone <your-repo-url>
cd investor-council-app

# Set up environment variables
cp .env.example .env
# Edit .env and paste your ALPHA_VANTAGE_API_KEY
```

### 2. Backend Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend
npm install
cd ..
```

## 🏃‍♂️ Usage

### 1. Run an Analysis
Use the Python script to fetch data and generate a report (in `analyses/`).
```bash
source venv/bin/activate
python3 main.py IBM
```
*Note: The free API tier has rate limits. The script includes delays to handle this.*

### 2. View the Dashboard
Start the Next.js viewer to see your reports.
```bash
cd frontend
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🧠 The Council Logic

| Investor | Core Metric | Logic Summary |
| :--- | :--- | :--- |
| **Buffett** | ROIC | Seeks durable moats ($ROIC > 15\%$) and conservative balance sheets. |
| **Lynch** | PEG Ratio | Buys growth at a reasonable price ($PEG < 1.0$). Categories: *Fast Grower*, *Stalwart*. |
| **Munger** | Lollapalooza | 1-10 Score. Rewards synergies between high returns, pricing power, and low debt. |
| **Dalio** | Macro | Evaluates inflation hedges and debt cycle positioning. |

## 📄 License
MIT
