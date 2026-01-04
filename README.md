# ReAct Agent with Tool Calling

## Description

Implements a ReAct (Reasoning + Acting) agent that can use tools to answer questions. The agent reasons about what tool to use, calls it with appropriate arguments, observes the results, and iterates until it arrives at a final answer. Demonstrates the tool-calling capabilities of LLMs using `.bind_tools()`.

## Tech Stack

- **LangChain** - Framework for building agents with tools
- **Azure OpenAI** - LLM provider with tool calling support
- **Python 3.12+** - Programming language

## Key Concepts

- **ReAct Pattern** - Reasoning → Acting → Observation cycle
- **Tool Binding** - Using `bind_tools()` to attach tools to LLM
- **Tool Calling** - LLM decides when and which tools to use
- **Agentic Loop** - Continuous loop that handles tool invocations and results
- **Callbacks** - Custom callback handler to observe LLM prompts and responses

## Project Files

- `main.py` - ReAct agent implementation with tool calling loop
- `callbacks.py` - Custom `AgentCallbackHandler` for observing agent behavior
- Sample tool: `get_text_length()` - Returns character count of text

## How It Works

1. User provides a question
2. LLM reasons about which tool to use
3. Agent executes the tool and gets results
4. Results are fed back to LLM for further reasoning
5. Loop continues until LLM provides final answer

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI key)
2. Run: `python main.py`