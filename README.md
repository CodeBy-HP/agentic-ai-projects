# ComplAI Sales Agent System

## Description

An AI-powered multi-agent system that generates and sends cold sales emails. The system uses multiple specialized agents to draft emails in different styles (professional, engaging, concise), evaluates them, and sends the best version to prospects via email.

## Tech Stack

- **Python 3.12+** - Core runtime
- **OpenAI Agents SDK** - Multi-agent orchestration
- **Azure Models** - LLM backend (configurable)
- **LangSmith** - Agent tracing and monitoring
- **SendGrid** - Email delivery service

## Key Concepts

- **Multi-Agent Workflow**: Separate agents for drafting, formatting, and management
- **Agent Orchestration**: Runner coordinates tasks and agent communication
- **Guardrails**: Input validation and safety checks
- **Async Processing**: Non-blocking execution with configurable max turns
- **Tracing**: Full observability via LangSmith integration

## Project Structure

```
.
├── main.py              # Entry point - runs the sales workflow
├── my_agents.py         # Agent definitions and setup
├── config.py            # Configuration and environment setup
├── prompts.py           # Agent prompts and templates
├── tools.py             # Function tools (send_html_email)
└── pyproject.toml       # Dependencies and project metadata
```

## Quick Start

### Prerequisites

- Python 3.12+
- API keys: Azure OpenAI, SendGrid, LangSmith (optional)

### Installation

```bash
pip install -e .
```

### Configuration

Create a `.env` file with:

```
AZURE_ENDPOINT=your_azure_endpoint
AZURE_API_KEY=your_azure_key
SENDGRID_API_KEY=your_sendgrid_key
EMAIL_FROM=sender@example.com
EMAIL_TO=recipient@example.com
LANGSMITH_API_KEY=your_langsmith_key  # optional
```

### Run

```bash
python main.py
```

The system will generate and send a cold sales email to the configured recipient.
