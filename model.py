from crewai import LLM
from dotenv import load_dotenv
load_dotenv()
import os
# groq_llm = LLM(
# model="groq/meta-llama/llama-4-scout-17b-16e-instruct",
# temperature=0.7
# )

venue_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",  # Ya "gemini/gemini-4-hydrogen"
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

logistics_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",  # Ya "gemini/gemini-4-hydrogen"
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)


marketing_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",  # Ya "gemini/gemini-4-hydrogen"
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)


