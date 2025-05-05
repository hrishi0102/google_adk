from google.adk.agents import Agent

root_agent = Agent(
   name="gweb_agent",
   model="gemini-2.0-flash",
   description="Greeting Agent",
   instruction="You are a helpful assistant. Ask for user's name and greet the user.",
)