import json
import atexit
import chainlit as cl
from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    Runner,
    set_default_openai_client,
    set_tracing_disabled,
)
import my_secrets

# 1. Load secrets
secrets = my_secrets.Secrets()

# 2. Configure Gemini client
client = AsyncOpenAI(
    api_key=secrets.api_key,
    base_url=secrets.api_url
)
set_default_openai_client(client)
set_tracing_disabled(True)

# 3. Initialize model and agent
model = OpenAIChatCompletionsModel(
    model=secrets.model,
    openai_client=client
)
agent = Agent(name="ChainlitGeminiAgent", model=model)
runner = Runner(agent)

# 4. In-memory conversation history
chat_history = []

@cl.on_message
async def main(message: str):
    # Record user message
    chat_history.append({"role": "user", "message": message})

    # Agent processes input
    result = await runner.run(message)
    response = getattr(result, "content", str(result))

    # Record and send bot response
    chat_history.append({"role": "bot", "message": response})
    await cl.send_message(response)

# 5. Persist chat history on exit
def save_history():
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=2)

atexit.register(save_history)