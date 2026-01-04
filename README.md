# Reflexion Agent

## Description

An advanced research agent that implements the Reflexion pattern - iteratively answering questions, reflecting on the response quality, searching for missing information, and revising answers with citations. The agent produces research-quality answers with numerical citations and reference lists, maximizing information accuracy and completeness.

## Tech Stack

- **LangGraph** - State graph for orchestrating multi-step workflows
- **LangChain** - Framework for chains and structured tools
- **Azure OpenAI** - LLM provider with tool calling
- **Tavily Search** - Web search for fact-finding and research
- **Pydantic** - Data validation for structured outputs
- **Python 3.12+** - Programming language

## Key Concepts

- **Reflexion Pattern** - Draft → Tool Use → Reflect → Revise loop
- **Self-Critique** - Agent identifies missing and superfluous information
- **Web Search Integration** - Searches for information to fill knowledge gaps
- **Structured Outputs** - Pydantic schemas for consistent response format
- **Citation Management** - Numerical citations and reference lists
- **Bounded Iterations** - Prevents infinite loops with MAX_ITERATIONS limit
- **Tool Calling** - LLM decides when and what to search for

## Project Structure

- `main.py` - Graph definition and workflow orchestration
- `chains.py` - LLM chains for initial drafting and revision
- `schemas.py` - Pydantic models for structured outputs
- `tool_executor.py` - Search tool integration and execution
- `flow.png` - Visual diagram of the workflow

## Workflow Stages

1. **Draft**: Initial ~250 word answer with self-critique
2. **Reflect**: Identify what's missing and what's superfluous
3. **Search**: Execute web searches based on identified gaps
4. **Revise**: Update answer with search results and citations
5. **Loop**: Repeat 2-4 until max iterations or quality threshold reached

## Output Format

- Detailed answer with word limit (~250 words)
- Reflection section (missing/superfluous info)
- Search queries for improvements
- References section with numbered citations

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI and Tavily keys)
2. Run: `python main.py`
3. View workflow diagram: `flow.png`