import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# Retrieve from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_url = os.getenv("GEMINI_API_URL")
gemini_api_model = os.getenv("GEMINI_API_MODEL")

# Validate
if not gemini_api_key or not gemini_api_url or not gemini_api_model:
    raise RuntimeError("Please set GEMINI_API_KEY, GEMINI_API_URL, and GEMINI_API_MODEL in your .env file")

class Secrets:
    def __init__(self):
        self.api_key = gemini_api_key
        self.api_url = gemini_api_url
        self.model = gemini_api_model