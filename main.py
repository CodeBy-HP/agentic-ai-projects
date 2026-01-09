from config import Config, initialize_azure_client

initialize_azure_client()

import asyncio
from agents import Runner
from agents import set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor
from my_agents import search_agent, planner_agent, email_agent, writer_agent
from schemas import WebSearchPlan, ReportData, WebSearchItem


async def plan_searches(query: str):
    """Use the planner_agent to plan which searches to run for the query"""
    print("Planning searches...")
    result = await Runner.run(planner_agent, f"Query: {query}")
    print(f"Will perform {len(result.final_output.searches)} searches")
    return result.final_output


async def perform_searches(search_plan: WebSearchPlan):
    """Call search() for each item in the search plan"""
    print("Searching...")
    tasks = [asyncio.create_task(search(item)) for item in search_plan.searches]
    results = await asyncio.gather(*tasks)
    print("Finished searching")
    return results


async def search(item: WebSearchItem):
    """Use the search agent to run a web search for each item in the search plan"""
    input = f"Search term: {item.query}\nReason for searching: {item.reason}"
    result = await Runner.run(search_agent, input)
    return result.final_output


async def write_report(query: str, search_results: list[str]):
    """Use the writer agent to write a report based on the search results"""
    print("Thinking about report...")
    input = f"Original query: {query}\nSummarized search results: {search_results}"
    result = await Runner.run(writer_agent, input)
    print("Finished writing report")
    return result.final_output


async def send_email(report: ReportData):
    """Use the email agent to send an email with the report"""
    print("Writing email...")
    result = await Runner.run(email_agent, report.markdown_report)
    print("Email sent")
    return report


async def run_workflow(query: str):

    print("Starting research...")
    search_plan = await plan_searches(query)
    search_results = await perform_searches(search_plan)
    report = await write_report(query, search_results)
    await send_email(report)
    print("Hooray!")


async def main():
    query = "Latest AI Agent frameworks in 2025"
    await run_workflow(query)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
