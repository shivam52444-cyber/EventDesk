import os
from typing import Type
import httpx
import requests
from pydantic import BaseModel, Field
from crewai.tools import BaseTool, tool
import hitl


class FeasibilityInput(BaseModel):
    city: str = Field(..., description="Target city name (e.g., 'Ballia', 'Goa', 'Lucknow')")
    requested_feature: str = Field(..., description="Specific venue style or geographic feature requested by user (e.g., 'sea-facing hotel', 'beach resort', 'rooftop banquet')")


class FeasibilityCheckTool(BaseTool):
    name: str = "Verify Location & Venue Feasibility"
    description: str = (
        "MUST be called FIRST before searching for venues. "
        "Checks via live Google Search whether the requested venue type or geographic feature "
        "(such as sea-facing, beach, mountain, snow, riverside) actually exists in the target city. "
        "Use this to catch impossible requests like 'sea-facing hotel in Ballia' before making any plans."
    )
    args_schema: Type[BaseModel] = FeasibilityInput
    max_usage_count: int = 1

    def _format_results(self, city: str, requested_feature: str, data: dict) -> str:
        snippets = [
            f"- {item.get('title')}: {item.get('snippet')}"
            for item in data.get("organic", [])[:3]
        ]
        if not snippets:
            return f"FEASIBILITY ALERT: Zero Google results found for '{requested_feature}' in '{city}'. Ask the user for clarification."
        return f"Search results for '{requested_feature}' in '{city}':\n" + "\n".join(snippets)

    async def _arun(self, city: str, requested_feature: str) -> str:
        """Async non-blocking Google search jab crew.akickoff() chalta hai."""
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Search unavailable; rely strictly on real-world geography."
        query = f"{requested_feature} in {city}"
        try:
            async with httpx.AsyncClient(timeout=6.0) as client:
                res = await client.post(
                    "https://serper.dev",
                    headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
                    json={"q": query, "num": 3},
                )
                res.raise_for_status()
                return self._format_results(city, requested_feature, res.json())
        except Exception as e:
            return f"Verification search error: {e}"

    def _run(self, city: str, requested_feature: str) -> str:
        """Sync fallback agar kabhi sync kickoff() chale."""
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Search unavailable; rely strictly on real-world geography."
        query = f"{requested_feature} in {city}"
        try:
            res = requests.post(
                "https://serper.dev",
                headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
                json={"q": query, "num": 3},
                timeout=6
            )
            res.raise_for_status()
            return self._format_results(city, requested_feature, res.json())
        except Exception as e:
            return f"Verification search error: {e}"


def create_ask_human_tool(run_id: str, qa_log: list[str]):
    """Har user run ke liye ek fresh tool aur uski apni memory banata hai."""

    @tool("Ask Human Tool", max_usage_count=2)
    def ask_human_tool(question: str) -> str:
        """Use if requested location/feature does not exist in reality OR if critical details like exact event date, time, or RSVP link are missing.
        NEVER ask about catering or food menu. NEVER ask a question already answered in previous_human_answers."""
        ans = hitl.ask(question, channel="agent", run_id=run_id)
        qa_log.append(f"Q: {question} -> A: {ans}")
        return ans

    return ask_human_tool


