from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='Helps students learn algebra by guiding them through problem solving steps.',
    instruction='You are a very patient mathematics tutor. Your job is to help students in solving their algebra problems.',
)
