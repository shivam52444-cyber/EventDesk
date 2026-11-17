from crewai import Task
from agent import venue_coordinator, logistics_manager, marketing_agent
from sstate import VenueDetails, LogisticsPlan, MarketingPlan

# TASK 1: Venue Coordinator (Bina 'f' ke placeholders)
venue_task = Task(
    description=(
        "Find the best venue in {city} for '{event_topic}' ({description}) "
        "accommodating {guests} guests. Total overall event budget is {total_budget}. "
        "BUDGET & NEGOTIATION GUIDELINE: {venue_feedback}. "
        "Clearly verify whether the venue includes in-house catering in its cost or not."
    ),
    expected_output="Structured venue details with exact estimated_cost, included_facilities, and has_inhouse_catering.",
    output_pydantic=VenueDetails,
    agent=venue_coordinator
)

# TASK 2: Logistics Manager (Bina 'f' ke placeholders)
logistics_task = Task(
    description=(
        "Plan logistics for {guests} guests at the selected venue: {venue_info}. "
        "In-house catering included by venue: {has_inhouse_catering}. "
        "Catering preference: {catering_preference}. "
        "STRICT BUDGET CONSTRAINT: Your remaining budget is ONLY {remaining_budget}. "
        "RULES: "
        "1. If 'has_inhouse_catering' is True, food cost is already covered in the venue price (your food cost = 0); "
        "only budget for missing AV/sound/decor equipment not in 'included_facilities'. "
        "2. If 'has_inhouse_catering' is False, arrange both external catering and missing equipment within {remaining_budget}. "
        "3. If {remaining_budget} is insufficient for your required items, set 'is_within_budget' to False "
        "and explain in 'negotiation_feedback' how much minimum budget you need."
    ),
    expected_output="Logistics plan with strict remaining budget feasibility check.",
    output_pydantic=LogisticsPlan,
    agent=logistics_manager
)

# TASK 3: Marketing Agent (Bina 'f' ke placeholders)
marketing_task = Task(
    description=(
        "Create a promotional campaign and official invitation for '{event_topic}' ({description}). "
        "Venue Name: {venue_name}, Address: {venue_address}. "
        "Target capacity: {guests} attendees. Highlight key venue facilities in the invite."
    ),
    expected_output="Target audience, ready-to-send invitation message, and social media posts.",
    output_pydantic=MarketingPlan,
    agent=marketing_agent
)
