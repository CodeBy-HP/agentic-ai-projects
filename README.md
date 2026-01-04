# RAG Gist - Retrieval-Augmented Generation

## Description

A simplified Retrieval-Augmented Generation (RAG) implementation that loads documents, chunks them, stores them in a vector database, and retrieves relevant content to answer user questions. Demonstrates both traditional and LCEL-based approaches to building RAG pipelines.

## Tech Stack

- **LangChain** - Framework for RAG and LLM workflows
- **Azure OpenAI** - LLM and embedding models
- **Pinecone** - Vector database for semantic search
- **Python 3.12+** - Programming language

## Key Concepts

- **Document Loading** - Load and process text documents
- **Text Chunking** - Split documents into manageable chunks with overlap
- **Embeddings** - Convert text to vector representations for semantic search
- **Vector Store** - Pinecone for efficient similarity search and retrieval
- **RAG Pipeline** - Retrieve relevant documents and pass them as context to LLM
- **LCEL (LangChain Expression Language)** - Composable, streamable, async-ready chains

## Project Files

- `ingestion.py` - Document loading, chunking, and ingestion into Pinecone
- `main.py` - RAG query implementation with two approaches: non-LCEL and LCEL-based
- `mediumblog1.txt` - Sample document for ingestion

## Quick Start

1. Set up environment variables (`.env` with Azure OpenAI and Pinecone keys)
2. Run ingestion: `python ingestion.py`
3. Query: `python main.py`