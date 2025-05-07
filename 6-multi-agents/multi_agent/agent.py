from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search  

# IMP, CANNOT USE BUILTIN TOOLS AS SUBAGENTS. NEED TO WRAP AROUND AGENTTOOL.
search_agent = Agent(
   name="search_agent",
   model="gemini-2.0-flash",
   description="Agent to answer questions using Google Search.",
   instruction="""You are an expert researcher. You answer questions related to user queries with the help of Google Search
   and provide accurate and relevant information with sources.
   """,
   tools=[google_search]
)

idea_agent = Agent(
    name="idea_agent",
    model="gemini-2.0-flash",
    instruction=""" You are a creative startup idea generator.
    You generate startup ideas based on the user's prompt.""",
    description="Generates creative startup ideas based on the prompt.",
    output_key="generated_idea",  # Save result to state
)

marketing_agent = Agent(
    name="marketing_agent",
    model="gemini-2.0-flash",
    instruction=""" You are an expert marketing specialist.
    You generate marketing strategies based on the user's prompt.""",
    description="Generates marketing strategies based on the prompt.",
    output_key="marketing_strategy",  # Save result to state
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    instruction=""" You are a multi-functional agent.
    You coordinate between different agents to provide comprehensive solutions.""",
    description="Root agent that manages other agents.",
    sub_agents=[idea_agent, marketing_agent],
    tools=[AgentTool(search_agent)],  # Use AgentTool to wrap around the search_agent
    output_key="final_output",
)