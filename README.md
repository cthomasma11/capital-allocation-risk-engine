# capital-allocation-risk-engine

A Monte Carlo-based simulation engine for evaluating portfolio allocation decisions under uncertainty using downside risk metrics (VaR, CVaR, drawdown), scenario stress testing, and risk-adjusted recommendation frameworks.

## Objective
Given limited capital and uncertain outcomes, identify allocations that maximize expected value while controlling downside risk.

## Methods
- Monte Carlo simulation (1,000–10,000 trials)
- Scenario analysis (volatility spike, correlation breakdown, market shocks)
- Risk metrics:
  - Value at Risk (VaR)
  - Conditional Value at Risk (CVaR)
  - Max drawdown
  - Sharpe ratio
- Allocation comparison (conservative, balanced, aggressive)

## Folder Structure
- `data/` – raw and processed datasets
- `notebooks/` – step-by-step analyses
- `src/` – core Python modules
- `reports/` – charts, PDFs, decision memo
- `app/` – optional Streamlit visualization
- `tests/` – unit tests
- `docs/` – methodology, assumptions, limitations

## Getting Started
1. Clone repo
2. Install dependencies:
```bash
pip install -r requirements.txt
