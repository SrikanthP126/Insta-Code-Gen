def build_mcp_context(task_type: str, language: str, user_level: str, user_input: str, history: list = None) -> str:
    """
    Builds a structured system prompt using Model Context Protocol (MCP) format.
    """
    context = f"""
You are a multilingual AI coding assistant.

Your task is to assist with: {task_type}
Target programming language: {language}
User skill level: {user_level}

Instructions:
- Be concise and clear.
- Provide examples or code when appropriate.
- Tailor response for a {user_level} developer.

"""

    if history:
        context += f"Chat History: {' | '.join(history)}\n"

    context += f"\nCurrent Prompt: {user_input}"
    return context.strip()
