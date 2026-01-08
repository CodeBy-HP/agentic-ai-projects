import asyncio
from agents import Runner, trace
from agents.tracing import set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor

from config import initialize_azure_client, Config
from my_agents import setup_all_agents


async def run_sales_workflow(message: str) -> str:
    """
    Run the complete sales email workflow.

    Args:
        message: The initial message/instruction for the sales workflow

    Returns:
        The final output from the workflow
    """
    sales_manager = setup_all_agents()

    with trace("Sales Manager Workflow"):
        result = await Runner.run(sales_manager, message, max_turns=Config.MAX_TURNS)
        return result.final_output


async def main():
    """Main function to initialize and run the sales agent system."""
    print("ComplAI Sales Agent System Starting...")

    initialize_azure_client()

    message = "Send a cold sales email addressed to 'Dear CEO'"

    final_output = await run_sales_workflow(message)

    print("\n" + "=" * 50)
    print("Workflow Complete!")
    print("=" * 50)
    print(final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])

    asyncio.run(main())
