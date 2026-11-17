from crewai.tools import tool


from gaurdrails import validate_with_lakera

@tool("Ask Human Tool", max_usage_count=2)
def ask_human_tool(question: str) -> str:
    """
    MANDATORY TOOL: Call this tool immediately whenever any required detail (such as exact event date, 
    time, indoor/outdoor preference, food menu, or RSVP link) is missing from the prompt. 
    Do NOT guess or use placeholders like [Insert Date]—always ask the user first using this tool.
    """
    max_retries = 3
    for attempt in range(max_retries):
        print(f"\n🤖 [AGENT QUESTION]: {question}")
        user_reply = input("👤 [YOUR ANSWER]: ").strip()

        # Check 1: Length cannot be less than 1 (Empty input block)
        if len(user_reply) < 1:
            print("⚠️ [Guardrail]: reply can't be less than 1, write a proper answer. Please try again.")
            continue

        # Check 2: Lakera Guard Prompt Injection Scan
        try:
            safe_reply = validate_with_lakera(user_reply, "Human Reply")
            return safe_reply
        except ValueError as e:
            print(f"\n{e}\n⚠️ it seems you want to inject a prompt or unsafe content. Please provide a safe and valid answer.")
            continue

    return "User did not provide a valid safe answer after 3 attempts. Proceed with safe defaults."
