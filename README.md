# Agentic RAG

## Description

An advanced Retrieval-Augmented Generation system built with LangGraph that combines document retrieval with agentic decision-making. The agent intelligently decides whether to retrieve documents, perform web searches, or generate answers based on query context. Uses a state-based graph architecture for controlled workflow execution.

## Tech Stack

- **LangChain** - Framework for building RAG systems
- **LangGraph** - State machine and workflow orchestration
- **Azure OpenAI** - LLM and embedding models
- **Chroma** - Vector database for document storage and retrieval
- **Tavily Search** - Web search integration for agentic decisions
- **Python 3.12+** - Programming language

## Key Concepts

- **Agentic RAG** - RAG with intelligent decision-making capabilities
- **LangGraph** - Graph-based state machine for workflow control
- **State Management** - GraphState to track question, generation, documents, and web search flags
- **Document Retrieval** - Vector similarity search with Chroma
- **Web Integration** - Conditional web search when documents are insufficient
- **Multi-Source Information** - Combines vector retrieval with web search results

## Project Structure

- `graph/` - Core workflow and state management
  - `state.py` - GraphState TypedDict for workflow state
  - `graph.py` - Main graph definition
  - `nodes/` - Individual workflow nodes
  - `chains/` - Reusable LLM chains
  - `consts.py` - Configuration constants
- `ingestion.py` - Document loading from web URLs and vector store creation
- `main.py` - Entry point for running queries

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI and Tavily keys)
2. Ingest documents: `python ingestion.py`
3. Run queries: `python main.py`