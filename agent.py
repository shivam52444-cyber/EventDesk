from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent
from model import venue_llm, logistics_llm, marketing_llm
from tool import create_ask_human_tool

from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent
from model import venue_llm, logistics_llm, marketing_llm
from tool import FeasibilityCheckTool, create_ask_human_tool


def create_venue_coordinator(run_id: str, qa_log: list[str]) -> Agent:
    return Agent(
        role="Venue Coordinator",
        goal="Verify geographic feasibility first, then find the best real venue matching the event topic, guests, and budget.",
        backstory=(
            "Strict, fact-based venue planner. You NEVER guess or invent fake venues. "
            "You always run 'Verify Location & Venue Feasibility' first to check if the requested feature exists in that city."
        ),
        tools=[
            FeasibilityCheckTool(),  # <-- Fresh instance per run, max_usage_count=1, clear schema!
            SerperDevTool(n_results=2, max_usage_count=3),
            ScrapeWebsiteTool(max_usage_count=2),
            create_ask_human_tool(run_id, qa_log)
        ],
        max_iter=10,
        llm=venue_llm,
        verbose=True
    )


def create_logistics_manager(run_id: str, qa_log: list[str]) -> Agent:
    return Agent(
        role="Logistics Manager",
        goal="Plan catering and equipment setup based on the selected venue.",
        backstory="Detail-oriented operations manager who arranges food and AV equipment.",
        tools=[
            SerperDevTool(n_results=2, max_usage_count=2),
            ScrapeWebsiteTool(max_usage_count=2),
            create_ask_human_tool(run_id, qa_log)
        ],
        max_iter=5,
        llm=logistics_llm,
        verbose=True
    )

def create_marketing_agent(run_id: str, qa_log: list[str]) -> Agent:
    return Agent(
        role="Marketing and Communications Agent",
        goal="Create promotional strategy and invitations for the event.",
        backstory="Creative marketer who crafts engaging event messages.",
        tools=[
            SerperDevTool(n_results=2, max_usage_count=2),
            ScrapeWebsiteTool(max_usage_count=1),
            create_ask_human_tool(run_id, qa_log)
        ],
        max_iter=5,
        llm=marketing_llm,
        verbose=True
    )
