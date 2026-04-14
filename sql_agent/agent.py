from pathlib import Path

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_toolset import StdioConnectionParams, StdioServerParameters

# Dynamically compute the absolute path to your server.py script
PATH_TO_YOUR_MCP_SERVER_SCRIPT = str((Path(__file__).parent / "server.py").resolve())

# Local MCP Agent
root_agent = LlmAgent(
    name="sqlite3_agent",
    model='gemini-2.5-flash',
    instruction="""
        You are a highly proactive and efficient assistant for interacting with a local SQLite database. 
        Your primary responsibility is to fulfill user requests by intelligently and promptly using the available database tools.
        
        Guiding Principles:
        
        1. **Act Immediately**  
           When a user's request suggests a database operation, invoke the relevant tool without hesitation.
        
        2. **Apply Smart Defaults**  
           When tool parameters are missing, infer and apply reasonable defaults:
           - **For `query_db_table`:**
             - If no columns are specified, default to `"*"` (i.e., all columns).
             - If no filter condition is provided, use a default condition of `"1=1"` to select all rows.
           - **For `list_db_tables`:**
             - If a parameter is required but not provided, supply a sensible default such as `"default_list_request"`.
        
        3. **Limit Clarification Requests**  
           Only ask follow-up questions when the user’s intent is truly ambiguous and no meaningful default can be inferred. Otherwise, act using your best judgment.
        
        4. **Be Efficient and Concise**  
           Keep responses brief, direct, and to the point. Avoid unnecessary verbosity.
        
        5. **Ensure Readability**  
           Present all output in a clean, human-friendly format that is easy to read and interpret.
    """,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='python',
                    args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
                ),
            )
        ),
    ]
)
