from pydantic import BaseModel, Field
from typing import List

# 1. Venue Task ka Output
class VenueDetails(BaseModel):
    venue_name: str = Field(description="Selected hotel or banquet hall name")
    address: str = Field(description="Full address of the venue")
    capacity: int = Field(description="Maximum guest capacity")
    estimated_cost: int = Field(description="Total venue booking cost as a plain integer (including food if has_inhouse_catering is True)")
    has_inhouse_catering: bool = Field(description="True if venue provides in-house catering within estimated_cost, False otherwise")
    included_facilities: List[str] = Field(description="Facilities already included like stage, projector, sound, parking")

# 2. Logistics Task ka Output (Budget Negotiation ke saath)
class LogisticsPlan(BaseModel):
    is_within_budget: bool = Field(description="True if required food (if any) and missing equipment fit inside remaining_budget, False if too low")
    negotiation_feedback: str = Field(description="If False, explain exact minimum budget needed for remaining items so Venue agent can find a cheaper hall")
    catering_menu_summary: str = Field(description="Recommended menu (or 'Included in Venue Package' if in-house)")
    catering_vendor: str = Field(description="In-house or external caterer details")
    equipment_list: List[str] = Field(description="Only missing AV, lighting, and seating equipment not provided by venue")
    estimated_logistics_cost: int = Field(description="Additional cost for external food (0 if in-house) + missing equipment as a plain integer")

# 3. Marketing Task ka Output
class MarketingPlan(BaseModel):
    target_audience: str = Field(description="Primary audience groups to target")
    invitation_message: str = Field(description="Ready-to-send invitation with exact venue name, address, and highlights")
    social_media_posts: List[str] = Field(description="2-3 promotional posts with relevant hashtags")


class EventState(BaseModel):
    event_topic: str = ""
    description: str = ""
    city: str = ""
    guests: int = 0
    total_budget: int = 0
    
    venue_feedback: str = (
        "Initial Guideline: If the venue INCLUDES in-house catering within its price, "
        "you may spend up to 75-80% of total_budget. If the venue DOES NOT include catering, "
        "strictly keep venue cost under 45-50% of total_budget so enough funds remain for external catering and equipment."
    )
    negotiation_attempts: int = 0
    max_negotiations: int = 3  # <-- Yahan se aap back-and-forth limit control kar sakte hain!
    catering_preference: str = "Venue In-house Catering"
    
    venue_info: dict = {}
    logistics_info: dict = {}
    marketing_info: dict = {}