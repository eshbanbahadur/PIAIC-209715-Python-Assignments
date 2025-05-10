# os module provides operating system interfaces, used here to read environment variables
import os

# Import core classes from the OpenAI Agents SDK
from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Runner,
    set_default_openai_client,
    set_tracing_disabled,
)
# Load environment variables from a .env file into os.environ
from dotenv import load_dotenv

# Read .env values (e.g. GEMINI_API_KEY) into environment
load_dotenv()

# Retrieve the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the async client pointing to Gemini's OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Configure the SDK to use our client by default, and turn off request tracing
set_default_openai_client(external_client)
set_tracing_disabled(True)

# Wrap the client in an OpenAIChatCompletionsModel for chat-style interactions
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)


def my_first_agent():
    """A simple Hello World agent using the OpenAI Agents SDK."""
   
        # Build an agent that always replies with exactly "Hello, world!"
    agent = Agent(
        name="hello-world-agent",
        instructions="You are an agent that responds with exactly 'Hello, world!' when prompted.",
        model=model,
    )

        # Run the agent synchronously on a simple prompt
    result = Runner.run_sync(agent, "Say Hello, world!")
    print(result.final_output)

# If you ever want to run this file directly, uncomment the guard below:
#if __name__ == "__main__":
#    my_first_agent()  # ✅ Now it's defined!
