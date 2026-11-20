import hashlib
import os
import re
import redis
import requests
from dotenv import load_dotenv

load_dotenv()

LAKERA_API_KEY = os.getenv("LAKERA_GUARD_API_KEY")
LAKERA_URL = "https://lakera.ai"
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Fast local jailbreak / off-topic patterns
_INJECTION_PATTERNS = re.compile(
    r"(ignore|forget|disregard)\s+(all\s+)?(previous\s+|your\s+)?(instructions?|rules?|prompts?)"
    r"|system\s*prompt|write\s+(a\s+)?code|python\s+code|act\s+as\s+",
    re.I,
)

try:
    rdb = redis.from_url(REDIS_URL, decode_responses=True, socket_connect_timeout=1)
except Exception:
    rdb = None


def _cache_key(text: str) -> str:
    digest = hashlib.sha256(text.strip().lower().encode("utf-8")).hexdigest()
    return f"lakera:human_reply:{digest}"


def validate_with_lakera(text: str, field_name: str = "input", use_cache: bool = False) -> str:
    if not text or not text.strip():
        return text

    clean_text = text.strip()
    key = _cache_key(clean_text)

    # 1. Redis Cache Check
    if use_cache and rdb is not None:
        try:
            verdict = rdb.get(key)
            if verdict == "safe":
                return clean_text
            if verdict == "blocked":
                raise ValueError(
                    f"🚨 Security Alert: '{field_name}' Suspicious or off-topic content detected!"
                )
        except redis.RedisError:
            pass

    # 2. Local Jailbreak / Off-topic Check (Lakera se pehle)
    if _INJECTION_PATTERNS.search(clean_text):
        if use_cache and rdb is not None:
            try:
                rdb.set(key, "blocked")
            except redis.RedisError:
                pass
        raise ValueError(
            f"🚨 Security Alert: '{field_name}' Suspicious or off-topic content detected!"
        )

    if not LAKERA_API_KEY:
        return clean_text

    # 3. Live Lakera Guard API Call
    try:
        response = requests.post(
            LAKERA_URL,
            headers={"Authorization": f"Bearer {LAKERA_API_KEY}"},
            json={
                "messages": [{"role": "user", "content": clean_text}],
                "breakdown": True
            },
            timeout=5
        )
        response.raise_for_status()
        result = response.json()
        flagged = bool(result.get("flagged", False))

        if use_cache and rdb is not None:
            try:
                rdb.set(key, "blocked" if flagged else "safe")
            except redis.RedisError:
                pass

        if flagged:
            raise ValueError(
                f"🚨 Security Alert (Lakera Guard): '{field_name}' Suspicious or unsafe content detected!"
            )

        return clean_text

    except requests.RequestException as e:
        raise RuntimeError(f"Guardrail service unreachable: {e}")
