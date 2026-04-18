import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams


GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

root_agent = Agent(
    model="gemini-2.5-flash",
    name="github_agent",
    instruction="Help users get information from GitHub",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://api.githubcopilot.com/mcp",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "all",
                    "X-MCP-Readonly": "true",
                    "Accept": "application/json, text/event-stream"
                },
            ),
        )
    ],
)