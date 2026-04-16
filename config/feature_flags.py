# ─────────────────────────────────────────────────────────
# HYDRA — Feature Flags (Kill Switches)
# THE ONLY place to turn features on/off.
# Never put kill switches inside any other file.
# ─────────────────────────────────────────────────────────

FEATURES = {

    # ── PATTERNS ──────────────────────────────────────────
    # V1 Confirmed
    "up_tri":               False,
    "down_tri":             False,
    "bull_proxy":           False,

    # Breakout Family
    "horizontal":           False,
    "squeeze":              False,
    "52w_high":             False,

    # Pullback Family
    "higher_low":           False,
    "ema_pullback":         False,
    "fib_ret":              False,
    "vwap_reclaim":         False,
    "order_block":          False,

    # Momentum Family
    "rs_break":             False,
    "vol_surge":            False,
    "adx_break":            False,

    # Mean Reversion Family
    "oversold":             False,
    "boll_squeeze":         False,
    "gap_fill":             False,
    "reversal":             False,
    "fvg":                  False,

    # ── DOMAINS ───────────────────────────────────────────
    "backtest_lab":         False,
    "decision_engine":      False,
    "execution_engine":     False,
    "smart_alerts":         False,
    "broker_integration":   False,

    # ── INTELLIGENCE ──────────────────────────────────────
    "news_filter":          False,
    "global_context":       False,
    "psychology_engine":    False,

    # ── QUANT ─────────────────────────────────────────────
    "quant_basic":          False,
    "quant_statistical":    False,
    "quant_risk":           False,
    "quant_simulation":     False,
    "quant_ml":             False,
    "quant_deep_learning":  False,

    # ── SYSTEM ────────────────────────────────────────────
    "overseer":             False,
    "maintenance":          False,
    "dry_run":              True,   # Always True until live trading
}


def is_enabled(feature: str) -> bool:
    """Check if a feature is enabled."""
    return FEATURES.get(feature, False)
