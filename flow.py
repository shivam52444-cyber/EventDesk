import asyncio
from crewai import Crew
from crewai.flow.flow import Flow, start, listen, router, or_
import hitl
from agent import create_venue_coordinator, create_logistics_manager, create_marketing_agent
from task import create_venue_task, create_logistics_task, create_marketing_task
from sstate import EventState


async def _resolve_crew_output(res):
    """CrewOutput aur CrewStreamingOutput dono se final CrewOutput nikalta hai."""
    if hasattr(res, "__aiter__"):
        async for _ in res:
            pass
        return res.result
    if hasattr(res, "__iter__") and not hasattr(res, "pydantic"):
        for _ in res:
            pass
        return res.result
    return res


class EventManagementFlow(Flow[EventState]):
    def _qa_summary(self) -> str:
        return "\n".join(self.state.human_qa_history) if self.state.human_qa_history else "None yet."

    @start()
    @listen("renegotiate_venue")
    async def find_venue_step(self):
        self.state.negotiation_attempts += 1
        agent = create_venue_coordinator(self.state.run_id, self.state.human_qa_history)
        task = create_venue_task(agent)
        crew = Crew(agents=[agent], tasks=[task], verbose=True, cache=True)
        raw = await crew.akickoff(inputs={
            "city": self.state.city,
            "event_topic": self.state.event_topic,
            "description": self.state.description,
            "guests": self.state.guests,
            "total_budget": self.state.total_budget,
            "venue_feedback": self.state.venue_feedback,
            "previous_human_answers": self._qa_summary()
        })
        res = await _resolve_crew_output(raw)
        self.state.venue_info = res.pydantic.model_dump()

    @router(find_venue_step)
    def check_catering_router(self):
        if self.state.venue_info.get("has_inhouse_catering"):
            self.state.catering_preference = "Venue In-house Catering"
            return "proceed_to_logistics"
        return "need_human_catering_input"

    @listen("need_human_catering_input")
    async def ask_human_catering(self):
        self.state.catering_preference = await asyncio.to_thread(
            hitl.ask,
            f"{self.state.venue_info.get('venue_name')} doesn't include catering. "
            "What kind of food should we arrange (veg / non-veg / buffet)?",
            channel="flow",
            kind="choice",
            options=["Veg buffet", "Non-veg buffet", "Veg and non-veg buffet", "Jain"],
            run_id=self.state.run_id
        )

    @listen(or_("proceed_to_logistics", ask_human_catering))
    async def run_logistics_step(self):
        venue_cost = self.state.venue_info.get("estimated_cost", 0)
        remaining_budget = self.state.total_budget - venue_cost
        agent = create_logistics_manager(self.state.run_id, self.state.human_qa_history)
        task = create_logistics_task(agent)
        crew = Crew(agents=[agent], tasks=[task], verbose=True, cache=True)
        raw = await crew.akickoff(inputs={
            "guests": self.state.guests,
            "venue_info": str(self.state.venue_info),
            "has_inhouse_catering": self.state.venue_info.get("has_inhouse_catering"),
            "catering_preference": self.state.catering_preference,
            "remaining_budget": remaining_budget,
            "previous_human_answers": self._qa_summary()
        })
        res = await _resolve_crew_output(raw)
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
    async def run_marketing_step(self):
        agent = create_marketing_agent(self.state.run_id, self.state.human_qa_history)
        task = create_marketing_task(agent)
        crew = Crew(agents=[agent], tasks=[task], verbose=True, cache=True)
        raw = await crew.akickoff(inputs={
            "event_topic": self.state.event_topic,
            "description": self.state.description,
            "venue_name": self.state.venue_info.get("venue_name"),
            "venue_address": self.state.venue_info.get("address"),
            "guests": self.state.guests,
            "previous_human_answers": self._qa_summary()
        })
        res = await _resolve_crew_output(raw)
        self.state.marketing_info = res.pydantic.model_dump()
        return {
            "venue": self.state.venue_info,
            "logistics": self.state.logistics_info,
            "marketing": self.state.marketing_info
        }
