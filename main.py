import asyncio
import logging
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_core import EVENT_LOGGER_NAME
from autogen_ext.models.openai import OpenAIChatCompletionClient

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."


openai_model_client = OpenAIChatCompletionClient(
    model="gpt-4.1-nano",
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = AssistantAgent(
    name="assistant",
    model_client=openai_model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks.",
)


async def main():
    result = await agent.run(task="Find information on AutoGen")
    print(result.messages)


asyncio.run(main())
