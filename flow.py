from crewai import Crew
from crewai.flow.flow import Flow, start, listen, router, or_
import hitl
from crewai.flow import (
    Flow,
    human_feedback,
    HumanFeedbackPending,
    HumanFeedbackProvider,
    HumanFeedbackResult
)
from crewai.flow.flow import start, listen, router, or_

from agent import venue_coordinator, logistics_manager, marketing_agent
from task import venue_task, logistics_task, marketing_task
from sstate import EventState
from tool import get_qa_summary, reset_qa_log
class APIFeedbackProvider(HumanFeedbackProvider):
    def request_feedback(self, context, flow):
        raise HumanFeedbackPending(context=context)

class EventManagementFlow(Flow[EventState]):
    @start()
    @listen("renegotiate_venue")
    def find_venue_step(self):
        if self.state.negotiation_attempts == 0:
            reset_qa_log()  # Naye run ki shuruat mein purana log saaf karein
        self.state.negotiation_attempts += 1
        
        crew = Crew(agents=[venue_coordinator], tasks=[venue_task], verbose=True)
        res = crew.kickoff(inputs={
            "city": self.state.city,
            "event_topic": self.state.event_topic,
            "description": self.state.description,
            "guests": self.state.guests,
            "total_budget": self.state.total_budget,
            "venue_feedback": self.state.venue_feedback,
            "previous_human_answers": get_qa_summary()  # <-- Renegotiation mein purane answers milenge
        })
        self.state.venue_info = res.pydantic.model_dump()
        self.state.human_qa_history = get_qa_summary().splitlines()

    @router(find_venue_step)
    def check_catering_router(self):
        if self.state.venue_info.get("has_inhouse_catering"):
            self.state.catering_preference = "Venue In-house Catering"
            return "proceed_to_logistics"
        return "need_human_catering_input"

    @listen("need_human_catering_input")
    def ask_human_catering(self):
        self.state.catering_preference = hitl.ask(
            f"{self.state.venue_info.get('venue_name')} doesn't include catering. "
            "What kind of food should we arrange (veg / non-veg / buffet)?",
            channel="flow", kind="choice",
            options=["Veg buffet", "Non-veg buffet", "Veg and non-veg buffet", "Jain"])

    @listen(or_("proceed_to_logistics", ask_human_catering))
    def run_logistics_step(self):
        venue_cost = self.state.venue_info.get("estimated_cost", 0)
        remaining_budget = self.state.total_budget - venue_cost
        
        crew = Crew(agents=[logistics_manager], tasks=[logistics_task], verbose=True)
        res = crew.kickoff(inputs={
            "guests": self.state.guests,
            "venue_info": str(self.state.venue_info),
            "has_inhouse_catering": self.state.venue_info.get("has_inhouse_catering"),
            "catering_preference": self.state.catering_preference,
            "remaining_budget": remaining_budget
            "previous_human_answers": get_qa_summary()

        })
        self.state.logistics_info = res.pydantic.model_dump()

    @router(run_logistics_step)
    def budget_negotiation_router(self):
        is_ok = self.state.logistics_info.get("is_within_budget", True)
        if not is_ok and self.state.negotiation_attempts < self.state.max_negotiations:
            self.state.venue_feedback = (
                f"REJECTED BY LOGISTICS (Attempt {self.state.negotiation_attempts}): "
                f"{self.state.logistics_info.get('negotiation_feedback')}. "
                f"Find a cheaper venue than {self.state.venue_info.get('estimated_cost')}!"
            )
            return "renegotiate_venue"
        return "budget_approved"

    @listen("budget_approved")
    def run_marketing_step(self):
        crew = Crew(agents=[marketing_agent], tasks=[marketing_task], verbose=True)
        res = crew.kickoff(inputs={
            "event_topic": self.state.event_topic,
            "description": self.state.description,
            "venue_name": self.state.venue_info.get("venue_name"),
            "venue_address": self.state.venue_info.get("address"),
            "guests": self.state.guests
            "previous_human_answers": get_qa_summary()
        })
        self.state.marketing_info = res.pydantic.model_dump()
        
        return {
            "venue": self.state.venue_info,
            "logistics": self.state.logistics_info,
            "marketing": self.state.marketing_info
        }
