from config import Config
from agents import Agent, function_tool
from agents.model_settings import ModelSettings
from prompts import search_agent_instructions, planner_agent_instructions
from tavily import TavilyClient
from schemas import WebSearchPlan


@function_tool
def search_web(query: str) -> str:
    """
    Searches the web for the given query using Tavily API.

    Args:
        query: The search query string.

    Returns:
        String of top 5 search results, or "No results found." if empty.
    """
    print(f"DEBUG: Searching for '{query}'...")
    tavily = TavilyClient()
    response = tavily.search(query=query, max_results=5)

    results = response.get("results", [])

    if not results:
        return "No results found."

    formatted_output = []
    for r in results:
        entry = (
            f"Title: {r.get('title', 'N/A')}\n"
            f"Source: {r.get('url', 'N/A')}\n"
            f"Content: {r.get('content', 'N/A')}"
        )
        formatted_output.append(entry)

    return "\n\n---\n\n".join(formatted_output)


search_agent = Agent(
    name="Search agent",
    instructions=search_agent_instructions,
    tools=[search_web],
    model=Config.AZURE_MODEL,
    model_settings=ModelSettings(tool_choice="required"),
)

planner_agent = Agent(
    name="PlannerAgent",
    instructions=planner_agent_instructions,
    model=Config.AZURE_MODEL,
    output_type=WebSearchPlan,
)
