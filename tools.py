from dotenv import load_dotenv
import os

load_dotenv(override=True)

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

if __name__ == "__main__":
    send_push_notification.invoke({"text": "Hello, me"})
