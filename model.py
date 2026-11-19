from crewai import LLM
from dotenv import load_dotenv
load_dotenv(override=True)
import os
# groq_llm = LLM(
# model="groq/meta-llama/llama-4-scout-17b-16e-instruct",
# temperature=0.7
# )
venue_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_rpm=8
)

logistics_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_rpm=8
)

marketing_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_rpm=8
)
