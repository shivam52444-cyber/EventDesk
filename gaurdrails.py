import os
import requests
from dotenv import load_dotenv

load_dotenv()

LAKERA_API_KEY = os.getenv("LAKERA_GUARD_API_KEY")
LAKERA_URL = "https://api.lakera.ai/v2/guard"

def validate_with_lakera(text: str, field_name: str = "input") -> str:

    if not text or not text.strip():
        return text

    #
    if not LAKERA_API_KEY:
        print("⚠️ Warning: LAKERA_GUARD_API_KEY missing in .env")
        return text.strip()

    try:
        response = requests.post(
            LAKERA_URL,
            headers={"Authorization": f"Bearer {LAKERA_API_KEY}"},
            json={
                "messages": [{"role": "user", "content": text}],
                "breakdown": True
            },
            timeout=5  
        )
        response.raise_for_status()
        result = response.json()

        
        if result.get("flagged", False):
            raise ValueError(
                f"🚨 Security Alert (Lakera Guard): '{field_name}' A suspiciour or unsafe content detected!"
            )

        return text.strip()

    except requests.RequestException as e:
        raise RuntimeError(f"Guardrail service unreachable: {e}")
