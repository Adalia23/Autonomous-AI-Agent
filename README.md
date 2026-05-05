# Autonomous AI Agent

An autonomous AI agent that takes a high-level goal, breaks it into steps, and uses tools to complete it — powered by **LangGraph**, **Gemini 1.5 Flash**, and **Tavily Search**.

![Python](https://img.shields.io/badge/Python-3.13-blue) ![LangGraph](https://img.shields.io/badge/LangGraph-latest-green) ![Gemini](https://img.shields.io/badge/Gemini-1.5%20Flash-orange) ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

## What It Does

Give the agent any goal in plain English — it autonomously decides which tools to use, executes them in sequence, and returns a structured, well-researched answer.

**Example goals:**
- "Research the latest AI agent trends and summarize the top 5"
- "Find the latest news about UAE tech startups"
- "Compare LangChain vs LangGraph for building agents"
- "What are the best Python libraries for ML in 2025?"

## Architecture
User Goal
↓
LangGraph ReAct Agent
↓
┌─────────────────────────────────┐
│         Tool Selection          │
├──────────┬──────────┬───────────┤
│  Search  │  Calc    │  Summary  │
│  (Tavily)│  (eval)  │  (NLP)    │
└──────────┴──────────┴───────────┘
↓
Gemini 1.5 Flash (Reasoning)
↓
Structured Result

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | LangGraph (ReAct pattern) |
| LLM | Google Gemini 1.5 Flash |
| Web Search | Tavily Search API |
| UI | Streamlit |
| Language | Python 3.13 |

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/Autonomous-AI-Agent.git
cd Autonomous-AI-Agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

- Get Gemini API key: https://aistudio.google.com/apikey
- Get Tavily API key: https://tavily.com

### 4. Run the app
```bash
streamlit run ui/app.py
```

## Project Structure

Autonomous-AI-Agent/
├── agent/
│   ├── agent.py          # LangGraph ReAct agent setup
│   └── init.py
├── tools/
│   ├── search_tool.py    # Tavily web search tool
│   ├── calculator_tool.py # Math expression evaluator
│   ├── summary_tool.py   # Text summarization tool
│   └── init.py
├── ui/
│   └── app.py            # Streamlit interface
├── .env                  # API keys (not committed)
├── requirements.txt
└── README.md

## How It Works

The agent uses the **ReAct (Reasoning + Acting)** pattern from LangGraph:

1. **Receives** a goal from the user
2. **Reasons** about which tools are needed
3. **Acts** by calling tools (search, calculate, summarize)
4. **Observes** the results
5. **Repeats** until the goal is achieved
6. **Returns** a structured final answer

## Demo

> Agent completing: *"Find the latest news about UAE tech startups"*

The agent searched the web, synthesized results from multiple sources, and returned a structured report with funding data, sector trends, and a summary table — all autonomously.

## Future Improvements

- Add memory so the agent remembers past conversations
- Add a code execution tool for data analysis tasks
- Deploy to Streamlit Cloud for public access
- Add support for file upload and document analysis