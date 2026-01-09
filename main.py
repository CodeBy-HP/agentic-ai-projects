from config import Config, initialize_azure_client

initialize_azure_client()

import asyncio
from agents import Runner
from agents import set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor
from my_agents import search_agent, planner_agent


async def run_workflow(message: str) -> str:

    result = await Runner.run(planner_agent, message, max_turns=Config.MAX_TURNS)
    return result.final_output


async def main():
    print("Hello from main func")

    message = "Latest AI Agent frameworks in 2025"
    final_output = await run_workflow(message)
    print(final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
