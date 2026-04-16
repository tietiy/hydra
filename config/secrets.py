# ─────────────────────────────────────────────────────────
# HYDRA — Secrets
# Single place to access all credentials.
# Imports from config.py — never from os directly.
# ─────────────────────────────────────────────────────────

from config.config import (
    SUPABASE_URL,
    SUPABASE_ANON_KEY,
    SUPABASE_SERVICE_KEY,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    ANTHROPIC_API_KEY,
    FIVEPAISA_APP_NAME,
    FIVEPAISA_APP_SOURCE,
    FIVEPAISA_USER_ID,
    FIVEPAISA_PASSWORD,
    FIVEPAISA_USER_KEY,
    FIVEPAISA_ENCRYPTION_KEY,
)


def get_supabase_creds() -> dict:
    return {
        "url": SUPABASE_URL,
        "anon_key": SUPABASE_ANON_KEY,
        "service_key": SUPABASE_SERVICE_KEY,
    }


def get_telegram_creds() -> dict:
    return {
        "token": TELEGRAM_BOT_TOKEN,
        "chat_id": TELEGRAM_CHAT_ID,
    }


def get_anthropic_creds() -> dict:
    return {
        "api_key": ANTHROPIC_API_KEY,
    }


def get_fivepaisa_creds() -> dict:
    return {
        "app_name": FIVEPAISA_APP_NAME,
        "app_source": FIVEPAISA_APP_SOURCE,
        "user_id": FIVEPAISA_USER_ID,
        "password": FIVEPAISA_PASSWORD,
        "user_key": FIVEPAISA_USER_KEY,
        "encryption_key": FIVEPAISA_ENCRYPTION_KEY,
    }
