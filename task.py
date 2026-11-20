from crewai import Task, Agent
from sstate import VenueDetails, LogisticsPlan, MarketingPlan


def create_venue_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Find the best venue in {city} for '{event_topic}' ({description}) "
            "accommodating {guests} guests. Total overall event budget is {total_budget}. "
            "BUDGET & NEGOTIATION GUIDELINE: {venue_feedback}. "
            "ALREADY ANSWERED BY USER: {previous_human_answers}. "
            "RULES: "
            "1. Clearly verify whether the venue includes in-house catering in its cost or not. "
            "2. Check 'ALREADY ANSWERED BY USER' first. NEVER ask a question that is already answered there. "
            "3. Do NOT ask about food/catering preferences (that is asked later in the flow). "
            "4. Only if exact event date, time, or RSVP link is missing from BOTH description and ALREADY ANSWERED BY USER, "
            "ask the user in a SINGLE combined question using 'Ask Human Tool'."
            "5. Extract the real 'website_url' and 'contact_info' (phone/email) directly from the search/scrape results. If not found, set them to 'Not listed'—NEVER guess or fabricate URLs or phone numbers."

        ),
        expected_output= " Extract the real 'website_url' and 'contact_info' (phone/email) directly from the search/scrape results. If not found, set them to 'Not listed'—NEVER guess or fabricate URLs or phone numbers.",
        output_pydantic=VenueDetails,
        agent=agent
    )


def create_logistics_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Plan logistics for {guests} guests at the selected venue: {venue_info}. "
            "In-house catering included by venue: {has_inhouse_catering}. "
            "Catering preference: {catering_preference}. "
            "ALREADY ANSWERED BY USER: {previous_human_answers}. "
            "STRICT BUDGET CONSTRAINT: Your remaining budget is ONLY {remaining_budget}. "
            "RULES: "
            "1. Do NOT ask the user questions already answered in ALREADY ANSWERED BY USER. "
            "2. If 'has_inhouse_catering' is True, food cost is already covered in the venue price (your food cost = 0); "
            "only budget for missing AV/sound/decor equipment not in 'included_facilities'. "
            "3. If 'has_inhouse_catering' is False, arrange both external catering and missing equipment within {remaining_budget}. "
            "4. If {remaining_budget} is insufficient for your required items, set 'is_within_budget' to False "
            "and explain in 'negotiation_feedback' how much minimum budget you need."
        ),
        expected_output="Logistics plan with strict remaining budget feasibility check.",
        output_pydantic=LogisticsPlan,
        agent=agent
    )


def create_marketing_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Create a promotional campaign and official invitation for '{event_topic}' ({description}). "
            "Venue Name: {venue_name}, Address: {venue_address}. "
            "Target capacity: {guests} attendees. Highlight key venue facilities in the invite. "
            "USER PROVIDED DETAILS (Date/Time/RSVP etc.): {previous_human_answers}. "
            "RULES: "
            "1. Use the exact date, time, and RSVP link from USER PROVIDED DETAILS if available. "
            "2. NEVER re-ask any question already answered in USER PROVIDED DETAILS. "
            "3. NEVER use placeholders like [Insert Date], [Insert Time], or [Insert Link]."
        ),
        expected_output="Target audience, ready-to-send invitation message, and social media posts.",
        output_pydantic=MarketingPlan,
        agent=agent
    )
