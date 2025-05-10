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


# Load environment variables
load_dotenv()

# Configure Gemini API client
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

# Set up AsyncOpenAI client pointing to Gemini's OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/ ",
)

# Use the Gemini model through the OpenAI interface
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Disable tracing for cleaner logs
set_default_openai_client(external_client)
set_tracing_disabled(True)


def finadvisor():
    """A finance-focused AI agent powered by Gemini."""
    
    # Define the agent
    agent = Agent(
        name="FinAdvisor",
        instructions="""
        You are FinAdvisor, a helpful and knowledgeable personal finance assistant.
        Your purpose is to help users understand and manage their finances better.

        Provide clear, accurate, and actionable advice on:
        - Budgeting and saving money
        - Investing basics
        - Managing debt
        - Setting financial goals

        Use simple language and avoid jargon.
        Always remind users that this is general advice, not personalized financial planning.
        End each response with a follow-up question or suggestion for further learning.
        """,
        model=model,
    )

    # Prompt user for input
    user_prompt = input("🏦 Enter your finance-related question: ")

    # Run the agent
    result = Runner.run_sync(agent, user_prompt)

    # Print final output
    print("\n📘 FinAdvisor Response:\n")
    print(result.final_output)

    # Save output to file
    with open("output.md", "w") as f:
        f.write(f"# FinAdvisor Response\n\n{result.final_output}")
    print("\n✅ Output saved to output.md")