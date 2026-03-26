import asyncio
import logging
import os

from autogen_core import EVENT_LOGGER_NAME
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

openai_model_client = OpenAIChatCompletionClient(
    model="gpt-4o-2024-08-06",
    api_key=os.getenv("OPENAI_API_KEY")
)


async def main() -> None:
    result = await openai_model_client.create([UserMessage(content="What is the capital of India?", source="user")])
    print(result)
    await openai_model_client.close()


asyncio.run(main())
