from google.adk.agents import Agent
from google.adk.tools import google_search  

root_agent = Agent(
   name="search_agent",
   model="gemini-2.0-flash",
   description="Agent to answer questions using Google Search.",
   instruction="""You are an expert researcher. You answer questions related to user queries.
   Here is some more information for you:
   name: {name}
   information: {description}
   """,
   tools=[google_search]
)