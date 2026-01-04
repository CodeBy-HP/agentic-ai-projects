# LangChain Documentation Helper

## Description

An interactive web application that answers questions about LangChain documentation. Users ask questions about LangChain, and the AI assistant retrieves relevant documentation from a vector store and generates contextual answers with source citations. Built with Streamlit for a user-friendly interface.

## Tech Stack

- **Streamlit** - Interactive web UI framework
- **LangChain** - Framework for RAG and agents
- **Azure OpenAI** - LLM and embedding models
- **Chroma/Pinecone** - Vector databases for documentation retrieval
- **Tavily Crawl** - Web crawling for document collection
- **Python 3.12+** - Programming language

## Key Concepts

- **Retrieval-Augmented Generation (RAG)** - Retrieve docs then generate answers
- **Vector Embeddings** - Convert documentation to embeddings for semantic search
- **Source Attribution** - Display source citations for retrieved documents
- **Chat Interface** - Conversational UI for querying documentation
- **Async Indexing** - Batch processing for efficient document ingestion
- **Agentic Retrieval** - LLM agent that decides how to retrieve and answer queries

## Project Structure

- `main.py` - Streamlit web application and chat interface
- `backend/core.py` - RAG pipeline and LLM agent logic
- `ingestion.py` - Document loading, chunking, and async indexing into vector store
- `logger.py` - Structured logging with colors for better visibility
- `mediumblog1.txt` - Sample documentation content

## Features

- **Chat Interface** - Multi-turn conversation with persistent session state
- **Source Citations** - Expandable sources panel showing document references
- **Document Retrieval** - Automatically retrieves most relevant documentation
- **Clear Session** - Button to reset conversation history
- **Error Handling** - Graceful error messages and exception display

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI and Pinecone/Chroma keys)
2. Ingest documentation: `python ingestion.py`
3. Run web app: `streamlit run main.py`
4. Open browser and start asking questions about LangChain!