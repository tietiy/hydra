# HYDRA — Architecture

## Identity
- **Name:** HYDRA
- **Type:** Cloud-First Lifetime Quant Trading Platform
- **Repo:** tietiy/hydra
- **Blueprint:** v3.0 (Approved April 12, 2026)

## Stack
| Component | Tool |
|-----------|------|
| Language | Python |
| Database | Supabase PostgreSQL |
| Compute | GitHub Actions |
| Dashboard | GitHub Pages |
| Alerts | Telegram |
| AI Brain | Claude API |
| Data | yfinance (→ 5paisa later) |
| Broker | 5paisa (Phase 11) |

## 5 Domains, 16 Layers

### Domain 0 — Command Center
- Layer 0: Overseer (monitor, heal, AI brain)
- Layer M: Maintenance Engine

### Domain 1 — Research Lab
- Layer 1: Backtest Lab
- Layer 1b: Backtest GUI
- Layer 6: Quant Engine (40+ models)

### Domain 2 — Trading Core
- Layer 2: Decision Engine (7-layer scoring)
- Layer 3: Execution Engine
- Layer 10: Smart Alerts
- Layer 12: Broker Integration

### Domain 3 — Intelligence
- Layer 4: News Intelligence
- Layer 9: Global Context
- Layer 7: Psychology Engine

### Domain 4 — Foundation
- Layer 5: Database
- Layer 8: Trade Review
- Layer 11: Tax & Compliance
- Layer 13: Goals & Progress
- Layer 14: Gamification

## 19 Patterns (4 Families)

| Family | Patterns |
|--------|----------|
| BREAKOUT | UP_TRI, DOWN_TRI, HORIZONTAL, SQUEEZE, 52W_HIGH |
| PULLBACK | BULL_PROXY, HIGHER_LOW, EMA_PULLBACK, FIB_RET, VWAP_RECLAIM, ORDER_BLOCK |
| MOMENTUM | RS_BREAK, VOL_SURGE, ADX_BREAK |
| MEAN_REVERSION | OVERSOLD, BOLL_SQUEEZE, GAP_FILL, REVERSAL, FVG |

## Build Philosophy
1. **Wrapper/Adapter** — never call data sources directly
2. **Modular files** — 100-200 lines max per file
3. **Kill switches** — config/feature_flags.py ONLY
4. **Auto-discovery** — new files picked up automatically
5. **Plug and play** — clone + fill .env = running system
6. **Dry run mode** — every function supports dry_run=True

## Trading Rules

### V1 Patterns (Confirmed)
- Entry: 9:15 AM next day
- Stop: Immediately after entry
- Exit: Open of Day 6
- Size: Max 5% capital
- Gap > 2x stop: Market order at open

### Universal Rules (All Patterns)
- No moving stop
- No adding to position
- Max 5% capital
- Stop hit = exit same day

### New Families
- All rules TBD via backtest

## Cost
- Hard cap: ₹3000/month
- Year 1-2: ₹500-2000/month
- Free: GitHub Actions, Supabase (500MB), Pages, Telegram
