import os
import asyncio

from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

#creating the agent
agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor',
    instruction="""You are a patient math tutor. Guide students through problems step-by-step. Don’t just give answers - help them discover solutions."""
)

APP_NAME = "math_tutor_app"
USER_ID = "student_1"
SESSION_ID = "session_001"

#creating the session
session_service = InMemorySessionService()

#the runner to run the app. the app contains the agent with memory
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service
)

# Step 6: Define async function to run the agent
async def run_agent():

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    print(f"Session created: {SESSION_ID}\n")

    user_message = Content(
        role="user",
        parts=[Part(text="How do I solve 2x + 5 = 13?")]
    )

    print("User: How do I solve 2x + 5 = 13?\n")
    print("Agent: ", end="")

    #run the async for loop
    async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=user_message

    ):
        # Print final response
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)


if __name__ == '__main__':
    asyncio.run(run_agent())
