import os
from langchain_community.chat_models import ChatOllama

# CRITICAL WARD: Forces Ollama to drop the model from RAM immediately after use.
os.environ["OLLAMA_KEEP_ALIVE"] = "0"

def get_llm(temperature: float = 0.7):
    """
    Summons the local AI model with strict hardware constraints.
    - temperature: Controls creativity (0.7 for debate, 0.0 for strict logic).
    """
    return ChatOllama(
        model="llama3.2:1b",     # Small 3B parameter model to fit in 8GB RAM
        temperature=temperature,
        num_ctx=2048,            # Restrict the AI's memory window to prevent crashes
        num_thread=6             # Dedicate 6 CPUs to AI, leaving 2 for your Operating System
    )