from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

# Load API key and configure Groq endpoint
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")  # Replace this or set in .env
GROQ_API_BASE = "https://api.groq.com/openai/v1"

# Initialize LangChain-compatible Groq LLM
llm = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url=GROQ_API_BASE,
    model="llama3-8b-8192",  # or "llama3-8b-8192"
    temperature=0.7
)

def get_llm_response(prompt: str, system_context: str = "You are a helpful coding assistant.") -> str:
    """
    Send a prompt and system context to Groq LLM and return response.
    """
    messages = [
        SystemMessage(content=system_context),
        HumanMessage(content=prompt)
    ]
    response = llm.invoke(messages)
    return response.content.strip()
