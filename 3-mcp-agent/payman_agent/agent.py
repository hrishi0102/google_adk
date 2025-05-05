# ./adk_agent_samples/mcp_agent/agent.py
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


async def create_agent():
  """Gets tools from MCP Server."""
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='node',
          args = ["/Users/hrishi0102/Developer/Experiments/payman_mcp/build/payman-server.js"]
      )
  )

  agent = LlmAgent(
      model='gemini-2.0-flash',
      name='enterprise_assistant',
      instruction=(
          'Help user in Payman related operations'
      ),
      tools=tools,
  )
  return agent, exit_stack


root_agent = create_agent()