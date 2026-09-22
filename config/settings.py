import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_MODEL_NAME: str = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")
    MEMORY_FILE: str = os.getenv("MEMORY_FILE", str(Path(__file__).resolve().parent.parent / "memory" / "profile_memory.json"))