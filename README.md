# Search Agent

## Description

A simple yet powerful search agent that uses web search to find information and return structured results with sources. The agent intelligently searches the web for user queries and returns answers along with the URLs of sources used. Perfect for building AI assistants that need real-time information from the web.

## Tech Stack

- **LangChain** - Framework for building agents
- **Google Generative AI (Gemini)** - LLM provider
- **Tavily Search** - Web search API integration
- **Pydantic** - Schema validation for structured outputs
- **Python 3.12+** - Programming language

## Key Concepts

- **Agent Pattern** - Intelligent agent that decides when to search
- **Web Search Integration** - Real-time information retrieval via Tavily
- **Structured Output** - Pydantic schemas for consistent response formatting
- **Source Attribution** - Tracking and returning URLs used in answers
- **Tool Integration** - Agent seamlessly uses search tools

## Project Files

- `main.py` - Agent setup and query execution
- Pydantic Models:
  - `AgentResponse` - Answer and sources structure
  - `Source` - URL and metadata for each source
- Tool: `TavilySearch()` - Web search functionality

## How It Works

1. User provides a query
2. Agent receives the message
3. Agent uses Tavily Search to find relevant information
4. Results are structured with answers and source URLs
5. Returns formatted response with citations

## Quick Start

1. Set up environment variables (`.env` with Google API key and Tavily API key)
2. Run: `python main.py`