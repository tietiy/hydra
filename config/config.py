# ─────────────────────────────────────────────────────────
# HYDRA — Config
# Loads environment variables and exposes them cleanly.
# All code imports from here. Never import os.environ directly.
# ─────────────────────────────────────────────────────────

import os
from dotenv import load_dotenv

# Auto-load .env file if present (local dev)
load_dotenv()


# ── SUPABASE ──────────────────────────────────────────────
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")

# ── TELEGRAM ──────────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# ── CLAUDE AI ─────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# ── 5PAISA (Phase 11) ─────────────────────────────────────
FIVEPAISA_APP_NAME = os.environ.get("FIVEPAISA_APP_NAME", "")
FIVEPAISA_APP_SOURCE = os.environ.get("FIVEPAISA_APP_SOURCE", "")
FIVEPAISA_USER_ID = os.environ.get("FIVEPAISA_USER_ID", "")
FIVEPAISA_PASSWORD = os.environ.get("FIVEPAISA_PASSWORD", "")
FIVEPAISA_USER_KEY = os.environ.get("FIVEPAISA_USER_KEY", "")
FIVEPAISA_ENCRYPTION_KEY = os.environ.get("FIVEPAISA_ENCRYPTION_KEY", "")

# ── ENVIRONMENT ───────────────────────────────────────────
ENV = os.environ.get("ENV", "development")
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() == "true"

IS_PRODUCTION = ENV == "production"
IS_DEVELOPMENT = ENV == "development"


def validate_config():
    """
    Validate all required environment variables are set.
    Called on system startup. Fails fast if anything missing.
    """
    required = {
        "SUPABASE_URL": SUPABASE_URL,
        "SUPABASE_ANON_KEY": SUPABASE_ANON_KEY,
        "SUPABASE_SERVICE_KEY": SUPABASE_SERVICE_KEY,
        "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
        "TELEGRAM_CHAT_ID": TELEGRAM_CHAT_ID,
        "ANTHROPIC_API_KEY": ANTHROPIC_API_KEY,
    }

    missing = [key for key, val in required.items() if not val]

    if missing:
        raise EnvironmentError(
            f"HYDRA STARTUP FAILED — Missing environment variables:\n"
            + "\n".join(f"  ❌ {key}" for key in missing)
            + "\n\nCopy .env.example to .env and fill in all values."
        )

    print("✅ HYDRA config validated — all environment variables present.")


def get_summary():
    """Returns a safe summary of config (no secrets)."""
    return {
        "env": ENV,
        "dry_run": DRY_RUN,
        "supabase_connected": bool(SUPABASE_URL),
        "telegram_connected": bool(TELEGRAM_BOT_TOKEN),
        "ai_connected": bool(ANTHROPIC_API_KEY),
        "broker_connected": bool(FIVEPAISA_APP_NAME),
    }
