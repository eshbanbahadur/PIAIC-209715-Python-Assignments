# 🤖 AI Chatbot with OpenAI Agent SDK & Chainlit

This is a robust, multi-LLM chatbot application built using the **Chainlit Starter Template** and enhanced with custom tools, real-time streaming, and persistent chat history. It demonstrates the use of the **OpenAI Agent SDK** with **Chainlit** to create a dynamic and modular AI assistant.

---

## ✅ Key Features

### 🚀 Chainlit Starter Template
- Rapid development scaffold for conversational agents.
- Built-in support for hot-reloading with the `-w` flag.

### 🧠 Multi-LLM Support
Easily switch between different large language models for performance and cost optimization:
- **Gemini** (Google)
- **GPT-4o-mini** (OpenAI)
- **GPT-3.5-turbo** (alias: gpt-40-mini)

LLMs are configured in `llm_config.json` and can be toggled during runtime.

### 🛠️ Built-in Custom Tools
Enhance your chatbot's capabilities with real-world data:

- **🌦 Current Weather** – Get weather info for any location.
- **📈 Stock Exchange Rates** – Query stock data using Alpha Vantage.
- **📰 Global News Headlines** – Fetch sentiment-based global news summaries.

All tools are created with the Agent SDK's `@tool` decorator and can be extended or customized.

### 📡 Streaming Responses
- Real-time response streaming (character-by-character) for a smooth and interactive experience.

### 💾 Chat History Storage
- All user conversations are saved in `chat_history.json` for later review, training, or debugging.

---

## 🧪 How to Run the Project

### 📦 Requirements

- Python 3.10+
- [uv](https://lithic.dev/uv) package manager
- API Keys for:
  - OpenAI
  - Google Gemini
  - Alpha Vantage (for stock and news tools)

### ▶️ Run Locally

```bash
uv run chainlit run chatbot.py -w
