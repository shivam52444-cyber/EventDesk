import sys
import asyncio

# Windows asyncio hang fix:
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from flow import EventManagementFlow
from formatedtext import print_formatted_plan

def    run_event_planner():
    # Bina persistence (database) ke Flow banayein
    flow = EventManagementFlow()
    
    user_inputs = {
        "event_topic": " marriage engagement ",
        "description": "A high profile meetup from diffrent places near beach",
        "city": "goa",
        "guests": 300,
        "total_budget": 1000000
    }
    
    print("Flow start ho raha hai...")
    # Agar catering missing hogi toh yeh khud terminal par ruk kar aapse jawab maangega
    result = flow.kickoff(inputs=user_inputs)
    
    print("\n=== FINAL EVENT PLAN ===")
    print_formatted_plan(result)

if __name__ == "__main__":
    run_event_planner()
