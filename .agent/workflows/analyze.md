---
description: Mission
---

---
name: "Run Investor Council Analysis"
description: "Executes a multi-agent financial deep dive on a specific ticker"
model: 
  name: "gemini-3-pro"
  temperature: 0.2
---

# Council Dispatcher Workflow

1. **Initialize:** - Create directory: `mkdir -p analyses/{{ticker}}`.
   - Create a `task.md` artifact to track progress for {{ticker}}.
2. **Fetch:** Call the `fetch-financials` skill for {{ticker}}. 
3. **Reason:** - Process the JSON data through the personas in `.agent/rules/council.md`.
   - **Explicit Task:** Instruct Agent Munger to calculate the **Lollapalooza Score (1-10)** based on the specific triggers defined in the rules.
4. **Parallel Save:** Generate four distinct files in `analyses/{{ticker}}/`:
   - `buffett.md`, `lynch.md`, `dalio.md`, `munger.md`.
5. **UI Build:** Create a high-end `analyses/{{ticker}}/index.html` using Tailwind CSS (via CDN) and Chart.js.
   - **Executive Summary Table:** At the top of the page, render a summary table with a `slate-900` background. It must display the Ticker, Current Price, and ROIC.
   - **Lollapalooza Spotlight:** Highlight the **Munger Lollapalooza Score (1-10)** and the final **Verdict** in a prominent row with a blue gradient background (`from-blue-900 to-slate-900`).
   - **Investor Cards:** Below the table, create a 2-column grid displaying the core findings from `buffett.md`, `lynch.md`, `dalio.md`, and `munger.md` as distinct cards.
   - **Data Visualization:** Use Chart.js to create a responsive bar chart comparing **Total Revenue** vs. **Net Income** over the last three years, pulling the data directly from the `income_statement` in the JSON payload.
   - **Styling:** Use $LaTeX$ for all financial formulas within the text to maintain a master-level analytical aesthetic.
   - In the index.html file, include a <script> block that uses Chart.js. Ensure the script maps the fiscalDateEnding, totalRevenue, and netIncome from the fetch-financials JSON to the chart. Style the chart using the slate and blue color palette to match the Tailwind UI.
6. **Verify:** Launch `analyses/{{ticker}}/index.html` in the integrated browser.