import os
import requests
from dotenv import load_dotenv

load_dotenv()

LAKERA_API_KEY = os.getenv("LAKERA_GUARD_API_KEY")
LAKERA_URL = "https://lakera.ai"

def validate_with_lakera(text: str, field_name: str = "input") -> str:
    """
    Lakera Guard API se check karta hai ki text mein Prompt Injection,
    Jailbreak, ya unsafe content toh nahi hai.
    """
    if not text or not text.strip():
        return text

    # Agar API key set nahi hai toh warning dekar aage badhein
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
            timeout=5  # 5 second timeout taaki app slow na ho
        )
        response.raise_for_status()
        result = response.json()

        # Agar Lakera ne text ko 'flagged: True' mark kiya (Prompt Injection detected!)
        if result.get("flagged", False):
            raise ValueError(
                f"🚨 Security Alert (Lakera Guard): '{field_name}' mein suspicious prompt injection ya unsafe content detect hua hai!"
            )

        return text.strip()

    except requests.RequestException as e:
        # Network error aane par fail-open ya fail-closed aap decide kar sakte hain
        raise RuntimeError(f"Guardrail service unreachable: {e}")
