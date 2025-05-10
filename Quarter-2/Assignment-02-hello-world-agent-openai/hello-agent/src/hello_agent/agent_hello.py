import os

from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Runner,
    set_default_openai_client,
    set_tracing_disabled,
)
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)


def my_first_agent():
    """A simple Hello World agent using the OpenAI Agents SDK."""
    agent = Agent(
        name="hello-world-agent",
        instructions="You are an agent that responds with exactly 'Hello, world!' when prompted.",
        model=model,
    )
    result = Runner.run_sync(agent, "Say Hello, world!")
    print(result.final_output)


if __name__ == "__main__":
    main()  # ✅ Now it's defined!
