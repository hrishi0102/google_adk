# Using In-Memory Session Storage

from google.adk.sessions import InMemorySessionService
from google.genai import types
from qa_agent.agent import search_agent
from google.adk.runners import Runner
from dotenv import load_dotenv
import uuid

load_dotenv()

session_service_stateful = InMemorySessionService()

# Additional context for agent using initial state
initial_state = {
    "name": "Payman AI",
    "description": "Payman AI is a personal assistant for Payman. Payman is a secure financial platform built specifically to let AI agents move money—without direct access to customer funds.",
}

# Create a session
APP_NAME = "payman"
USER_ID= "payman_user"
SESSION_ID = str(uuid.uuid4())
state_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)
print(f"Session created: {SESSION_ID}")

# Create a runner
runner = Runner(
    agent=search_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

# Mock messages
new_message = types.Content(role="user", parts=[types.Part(text="What is Payman?")])

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response:
        if event.content and event.content.parts:
            print(f"Final response: {event.content.parts[0].text}")

print("----------Session State----------")
session = session_service_stateful.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
)

print("----------Final Session State----------")
for key, value in session.state.items():
    print(f"{key}: {value}")