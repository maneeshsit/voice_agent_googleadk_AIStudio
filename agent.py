from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name='root_agent',
    model='gemini-2.0-flash-live-001',
    description='A helpful assistant for user questions',
    instruction='You are an AI News assistant. Use Google search to find about RandomTechAce YouTube channel',
    tools=[google_search]
)