from dotenv import load_dotenv
import os
import asyncio

load_dotenv(override=True)

from agents.tracing import set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor
from agents import Runner, trace
from sales_agent import sales_manager


async def main():
    print("Hello from projects!")
    message = "Send a cold sales email addressed to 'Dear CEO'"

    with trace("Sales manager"):
        result = await Runner.run(sales_manager, message, max_turns=6)
        print(result.final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
