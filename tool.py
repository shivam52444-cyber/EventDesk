from crewai.tools import tool
import hitl

def create_ask_human_tool(run_id: str, qa_log: list[str]):
    """Har user run ke liye ek fresh tool aur uski apni memory banata hai."""
    
    @tool("Ask Human Tool", max_usage_count=2)
    def ask_human_tool(question: str) -> str:
        """Use ONLY if critical details like exact event date, time, indoor/outdoor preference, or RSVP link are missing.
        NEVER ask about catering or food menu. NEVER ask a question already answered in previous_human_answers."""
        # run_id pass karne se sawal sirf isi user ki screen par jayega
        ans = hitl.ask(question, channel="agent", run_id=run_id)
        qa_log.append(f"Q: {question} -> A: {ans}")
        return ans

    return ask_human_tool

