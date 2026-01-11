from dotenv import load_dotenv
import os

load_dotenv(override=True)

import asyncio
from langchain.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
import requests

serper = GoogleSerperAPIWrapper()
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"


@tool
def search(query: str) -> str:
    """Useful for when you need more information from an online search."""
    return serper.run(query)


@tool
def send_push_notification(text: str):
    """Send a push notification to the user"""
    requests.post(
        pushover_url,
        data={"token": pushover_token, "user": pushover_user, "message": text},
    )


TOOLS = [send_push_notification, search]

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser


def run_playwright():
    sync_browser = create_sync_playwright_browser(headless=False)

    toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
    tools = toolkit.get_tools()

    tool_dict = {tool.name: tool for tool in tools}
    navigate_tool = tool_dict.get("navigate_browser")
    extract_text_tool = tool_dict.get("extract_text")

    navigate_tool.run({"url": "https://example.com", "timeout": 60000})
    text = extract_text_tool.run({})

    print(f"Extracted text: {text}")
    sync_browser.close()

    return tools


if __name__ == "__main__":
    browser_tools = run_playwright()
