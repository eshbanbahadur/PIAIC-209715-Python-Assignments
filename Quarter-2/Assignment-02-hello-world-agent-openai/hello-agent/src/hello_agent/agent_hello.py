# agent_hello.py

from agents import Agent, Runner


def my_first_agent():
    """A simple Hello World agent using the OpenAI Agents SDK."""
    agent = Agent(
        name="hello-world-agent",
        instructions="You are an agent that responds with exactly 'Hello, world!' when prompted.",
    )
    result = Runner.run_sync(agent, "Say Hello, world!")
    print(result.final_output)  # Expected output: Hello, world!


my_first_agent()
