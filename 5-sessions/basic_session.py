# Using In-Memory Session Storage

from google.adk.sessions imprt InMemorySessionService
from google.genai import types
from qa_agent import search_agent

load_dotenv()

session_service_stateful = InMemorySessionService()

# Additional context for agent using initial state
initial_state = {
    "name": "Payman AI",
    "description": "Payman AI is a personal assistant for Payman. Payman is a secure financial platform built specifically to let AI agents move money—without direct access to customer funds.",
}

