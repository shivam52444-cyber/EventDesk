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
        "event_topic": "AI & Startup Summit",
        "description": "A tech conference with keynote speakers and networking dinner",
        "city": "Ballia",
        "guests": 150,
        "total_budget": 50000
    }
    
    print("Flow start ho raha hai...")
    # Agar catering missing hogi toh yeh khud terminal par ruk kar aapse jawab maangega
    result = flow.kickoff(inputs=user_inputs)
    
    print("\n=== FINAL EVENT PLAN ===")
    print_formatted_plan(result)

if __name__ == "__main__":
    run_event_planner()
