# AI Research & Email Agent

A multi-agent system that automates research workflows by planning searches, gathering web data, generating reports, and sending emails.

## Description

This project orchestrates AI agents to process a user query by:
1. Planning multiple searches to effectively answer the query
2. Executing web searches using Tavily API
3. Synthesizing results into a structured report
4. Automatically sending the report via email

Perfect for automating research aggregation and distribution workflows.

## Tech Stack

- **OpenAI Agents SDK** - Agent orchestration and coordination
- **Tavily** - Web search capabilities
- **SendGrid** - Email delivery
- **LangSmith** - Agent tracing and monitoring
- **Python 3.12+** - Core runtime

## Key Concepts

- **Agent-based Architecture**: Multiple specialized agents handle different tasks (planning, searching, writing, emailing)
- **Async Orchestration**: Parallel search execution for efficiency
- **Tool Integration**: Agents use web search and email tools to accomplish goals
- **Structured Outputs**: Typed schemas ensure consistent data flow between agents

## Project Structure

```
.
├── main.py           # Orchestration and workflow entry point
├── my_agents.py      # Agent definitions and tools (search, email)
├── config.py         # Configuration and Azure client setup
├── prompts.py        # Agent instruction prompts
├── schemas.py        # Data models (WebSearchPlan, ReportData, etc.)
├── pyproject.toml    # Dependencies and project metadata
└── README.md         # This file
```

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -e .
   ```

2. **Configure Credentials**
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   SENDGRID_API_KEY=your_sendgrid_key
   AZURE_ENDPOINT=your_azure_endpoint
   AZURE_API_KEY=your_azure_key
   ```

3. **Run the System**
   ```python
   import asyncio
   from main import plan_searches, perform_searches, write_report, send_email

   async def main():
       plan = await plan_searches("Your research question here")
       results = await perform_searches(plan)
       report = await write_report("Your query", results)
       await send_email(report)

   asyncio.run(main())
   ```
