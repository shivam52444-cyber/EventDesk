from crewai.tools import tool
import hitl

# Current run ke Q&A track karne ke liye thread-safe/run-level list
_qa_log: list[str] = []

def reset_qa_log():
    _qa_log.clear()

def get_qa_summary() -> str:
    return "\n".join(_qa_log) if _qa_log else "None yet."

@tool("Ask Human Tool", max_usage_count=2)
def ask_human_tool(question: str) -> str:
    """Use ONLY if critical details like exact event date, time, indoor/outdoor preference, or RSVP link are missing.
    NEVER ask about catering or food menu (handled separately). NEVER ask a question already answered in previous_human_answers."""
    ans = hitl.ask(question, channel="agent")
    _qa_log.append(f"Q: {question} -> A: {ans}")
    return ans
