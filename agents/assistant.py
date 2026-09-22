import json
from langchain_core.messages import AIMessage
from llm.groq_llm import get_groq_llm
from config import ASSISTANT_PROMPT

llm = get_groq_llm()

from config.settings import settings

MEMORY_FILE = settings.MEMORY_FILE

def assistant_agent(state):
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except FileNotFoundError:
        memory = {}

    messages = state["messages"]

    system_prompt = ASSISTANT_PROMPT.format(memory=memory)

    response = llm.invoke(system_prompt + "\n" + messages[-1].content)

    return {
        "messages": [AIMessage(content=response.content)]
    }
