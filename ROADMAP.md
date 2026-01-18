# 🗺️ Project Roadmap

The **Investor Council** is evolving. Below is our high-level plan for future features and improvements.

## Phase 1: Foundation (Current)
- [x] **Core Data Layer**: Alpha Vantage integration for Income/Balance/Cash Flow.
- [x] **Council Logic**: Basic algorithms for Buffett (ROIC), Lynch (PEG), Munger (Score), Dalio (Macro).
- [x] **Presentation**: Next.js Dashboard with Markdown & LaTeX rendering.

## Phase 2: Enhanced Intelligence (Next Up)
- [ ] **Technical Analysis Module**: Add RSI, MACD, and Moving Averages to the data fetcher.
- [ ] **LLM Integration**: Use a local LLM (e.g., Gemma 2) or API to convert the numeric "Council Opinions" into a cohesive narrative summary.
- [ ] **Sector Benchmarking**: Compare target stock metrics against industry averages.

## Phase 3: Portfolio & Persistence
- [ ] **Database Integration**: Move from file-based `analyses/` to a SQLite/Postgres database (Supabase).
- [ ] **User Portfolios**: Allow users to save strict watchlists.
- [ ] **Historical Tracking**: Track how "Council Scores" change over time.

## Phase 4: UI/UX Polish
- [ ] **Interactive Charts**: Recharts/Visx integration for price history.
- [ ] **Export Options**: PDF export for reports.
- [ ] **Dark/Light Mode**: User-toggleable themes.

---
*Ideas or contributions? Feel free to open an issue!*
