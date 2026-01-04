# ReAct Function Calling with LangGraph

## Description

A ReAct agent implementation using LangGraph that demonstrates function calling capabilities. The agent reasons about which tools to use (web search, calculations), executes them, and loops until it reaches a final answer. Uses a state-based graph architecture for controlled, deterministic workflow execution.

## Tech Stack

- **LangGraph** - State graph framework for agentic workflows
- **LangChain** - Framework for tools and agent integration
- **Azure OpenAI** - LLM provider with function calling support
- **Tavily Search** - Web search tool integration
- **Python 3.12+** - Programming language

## Key Concepts

- **ReAct Pattern** - Reason → Act → Observe loop for task completion
- **LangGraph State Machine** - Graph-based workflow with deterministic control flow
- **Function Calling** - LLM calling tools via `.bind_tools()`
- **Tool Node** - LangGraph's `ToolNode` for automatic tool execution
- **Conditional Edges** - Routes based on whether agent called tools or finished
- **Message State** - Uses `MessagesState` to track conversation history

## Project Files

- `main.py` - Graph definition and workflow orchestration
- `nodes.py` - Agent reasoning node and tool execution setup
- `react.py` - LLM configuration and tool definitions
- `flow.png` - Visual diagram of the graph workflow
- Custom tools:
  - `TavilySearch()` - Web search
  - `triple()` - Math operation (multiplies number by 3)

## Workflow

1. **Reasoning Phase**: LLM analyzes question and decides which tools to use
2. **Acting Phase**: Selected tools are executed with appropriate inputs
3. **Loop**: Results fed back to LLM for continued reasoning until task complete
4. **Final Answer**: LLM provides final answer when no more tools needed

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI and Tavily keys)
2. Run: `python main.py`
3. View workflow diagram: `flow.png`