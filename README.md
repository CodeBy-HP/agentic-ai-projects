# ReAct Search Agent

## Description

A ReAct agent that leverages web search capabilities to find and retrieve information from the internet. The agent searches for relevant information, structures the response with sources, and returns both the answer and the URLs used. Perfect for building AI assistants that need real-time information from the web.

## Tech Stack

- **LangChain** - Framework for building agents
- **Google Generative AI (Gemini)** - LLM provider
- **Tavily Search** - Web search API integration
- **Pydantic** - Data validation and schema definitions
- **Python 3.12+** - Programming language

## Key Concepts

- **ReAct Pattern** - Reasoning → Acting → Observation loop for search tasks
- **Web Search Integration** - Using Tavily API for real-time web searches
- **Structured Output** - Pydantic schemas for consistent response formatting
- **Tool Strategy** - Controlling agent output format with `ToolStrategy`
- **Sources Tracking** - Extracting and returning URLs used in the answer

## Project Files

- `main.py` - Agent setup and invocation with search capability
- `schemas.py` - Pydantic models for structured response (`AgentResponse`, `Source`)
- `prompt.py` - ReAct prompt template with format instructions
- Tool: `TavilySearch()` - Web search tool for finding information

## How It Works

1. User provides a search query
2. Agent reasons about what information is needed
3. Agent performs web search using Tavily
4. Results are formatted into structured response with sources
5. Returns answer and list of source URLs

## Quick Start

1. Set up environment variables (`.env` with Google API key and Tavily API key)
2. Run: `python main.py`