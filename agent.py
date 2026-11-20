from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent
from model import venue_llm, logistics_llm, marketing_llm
from tool import create_ask_human_tool

def create_venue_coordinator(run_id: str, qa_log: list[str]) -> Agent:
    return Agent(
        role="Venue Coordinator",
        goal="Find the best venue matching the event topic, guests, and budget.",
        backstory="Expert venue planner who checks capacity, pricing, and whether in-house catering is included.",
        tools=[
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
