from dotenv import load_dotenv

load_dotenv(override=True)

from typing import Annotated
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
import requests
import os
from langchain_openai import ChatOpenAI
from typing import TypedDict


from langchain.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper

serper = GoogleSerperAPIWrapper()


@tool
def search(query: str) -> str:
    """Useful for when you need more information from an online search."""
    return serper.run(query)


if __name__ == "__main__":
    result = search.invoke({"query": "What is the capital of France?"})
    print(result)
