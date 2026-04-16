# ─────────────────────────────────────────────────────────
# HYDRA — Constants
# All fixed values used across the system.
# Never hardcode these anywhere else.
# ─────────────────────────────────────────────────────────

# ── PROJECT ───────────────────────────────────────────────
PROJECT_NAME = "HYDRA"
VERSION = "1.0.0"
BLUEPRINT_VERSION = "3.0"

# ── MARKET ────────────────────────────────────────────────
MARKET_OPEN = "09:15"
MARKET_CLOSE = "15:30"
PRE_MARKET_START = "09:00"
PRE_MARKET_END = "09:08"
EOD_UPDATE_TIME = "15:35"
MORNING_SCAN_TIME = "08:45"
TIMEZONE = "Asia/Kolkata"

# ── UNIVERSE ──────────────────────────────────────────────
UNIVERSE_FILE = "data/fno_universe.csv"
HOLIDAYS_FILE = "data/holidays.json"
SECTORS_FILE = "data/sectors.json"
TOTAL_STOCKS = 188

# ── TRADING RULES (V1 CONFIRMED) ──────────────────────────
MAX_CAPITAL_PER_TRADE = 0.05        # 5%
EXIT_DAY = 6                         # Open of Day 6
MIN_RR_RATIO = 1.5
STRONG_RR_RATIO = 2.0
GAP_MULTIPLIER = 2.0                 # Gap > 2x stop = market order

# ── SCORING ───────────────────────────────────────────────
SCORE_ELITE = 9
SCORE_STRONG = 7
SCORE_MODERATE = 5
SCORE_WEAK = 3

SCORE_ELITE_SIZE = 0.07             # 7% capital
SCORE_STRONG_SIZE = 0.05            # 5% capital
SCORE_MODERATE_SIZE = 0.03          # 3% capital
SCORE_WEAK_SIZE = 0.00              # Skip

# ── PATTERN VALIDATION THRESHOLDS ─────────────────────────
MIN_WIN_RATE = 0.65
MIN_PROFIT_FACTOR = 2.0
MIN_EXPECTANCY = 0.02
MAX_STOP_RATE = 0.25
MIN_TRADES = 100
MAX_P_VALUE = 0.01
WALK_FORWARD_PERIODS = 4

# ── BACKTEST ──────────────────────────────────────────────
BACKTEST_YEARS = 20
BACKTEST_START = "2004-01-01"

# ── COST CAP ──────────────────────────────────────────────
MONTHLY_COST_CAP_INR = 3000

# ── PATTERN FAMILIES ──────────────────────────────────────
PATTERN_FAMILIES = {
    "BREAKOUT":       ["up_tri", "down_tri", "horizontal", "squeeze", "52w_high"],
    "PULLBACK":       ["bull_proxy", "higher_low", "ema_pullback", "fib_ret", "vwap_reclaim", "order_block"],
    "MOMENTUM":       ["rs_break", "vol_surge", "adx_break"],
    "MEAN_REVERSION": ["oversold", "boll_squeeze", "gap_fill", "reversal", "fvg"],
}

# ── V1 CONFIRMED PATTERNS ─────────────────────────────────
V1_PATTERNS = ["up_tri", "down_tri", "bull_proxy"]

# ── REGIME ────────────────────────────────────────────────
REGIMES = ["BULL", "BEAR", "CHOPPY"]

# ── ALERTS ────────────────────────────────────────────────
ALERT_THROTTLE_SECONDS = 300        # 5 min between same alerts
ALERT_MAX_PER_HOUR = 10
