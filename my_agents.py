from config import Config
from agents import Agent, function_tool
from agents.model_settings import ModelSettings
from prompts import (
    search_agent_instructions,
    planner_agent_instructions,
    email_agent_instructions,
    write_agent_instruction,
)
from tavily import TavilyClient
from schemas import WebSearchPlan, ReportData
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict


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


@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send out an email with the given subject and HTML body.

    Args:
        subject: The email subject line
        html_body: The HTML formatted email body

    Returns:
        Dict containing the status of the email send operation
    """
    sg = sendgrid.SendGridAPIClient(api_key=Config.SENDGRID_API_KEY)
    from_email = Email(Config.EMAIL_FROM)
    to_email = To(Config.EMAIL_TO)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


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

email_agent = Agent(
    name="Email agent",
    instructions=email_agent_instructions,
    tools=[send_html_email],
    model=Config.AZURE_MODEL,
)


writer_agent = Agent(
    name="WriterAgent",
    instructions=write_agent_instruction,
    model="gpt-4o-mini",
    output_type=ReportData,
)
