# Reflection Agent

## Description

An AI agent that improves outputs through iterative reflection and refinement. The agent generates initial content (tweets in this example), receives critique from a "reflection" LLM, and iteratively improves the output based on feedback. Demonstrates the power of self-reflection loops for quality enhancement.

## Tech Stack

- **LangGraph** - State graph for managing reflection loops
- **LangChain** - Framework for prompts and chains
- **Azure OpenAI** - LLM provider
- **Python 3.12+** - Programming language

## Key Concepts

- **Reflection Loop** - Iterative generation → critique → refinement cycle
- **Dual Prompts** - Separate prompts for generation and reflection
- **Message State** - Uses `MessagesPlaceholder` to maintain conversation history
- **Conditional Stopping** - Stops after max iterations (6 messages)
- **Self-Improvement** - Agent refines output based on its own critique
- **LangGraph State Machine** - Graph-based control flow for structured loops

## Project Files

- `main.py` - Graph definition and reflection loop orchestration
- `chains.py` - LLM chains for generation and reflection
- `flow.png` - Visual diagram of the agent workflow

## How It Works

1. **Generation Phase**: LLM generates initial content (e.g., tweet)
2. **Reflection Phase**: LLM critiques the content and provides recommendations
3. **Refinement**: Previous generation + critique fed back to generate improved version
4. **Loop**: Process repeats until max iterations reached
5. **Final Output**: Best refined version returned

## Use Case Example

Input: Poorly written tweet about a feature
→ Agent generates improved version
→ Agent reflects and critiques the tweet
→ Agent generates refined version based on feedback
→ Repeat until high quality or max iterations reached

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI key)
2. Run: `python main.py`
3. View workflow diagram: `flow.png`