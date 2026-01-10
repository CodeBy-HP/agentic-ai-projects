from dotenv import load_dotenv

load_dotenv(override=True)

from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
import gradio as gr
import os
from langchain_openai import AzureChatOpenAI
from typing import TypedDict
from tools import TOOLS


class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)
llm_with_tools = llm.bind_tools(TOOLS)


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


def should_continue(state: State) -> Literal["tools", END]:
    """Route to tools if LLM made a tool call."""
    messages = state["messages"]
    last_message = messages[-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=TOOLS))

graph_builder.add_conditional_edges("chatbot", should_continue, ["tools", END])

graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()


def chat(user_input: str, history):
    from langchain.messages import HumanMessage

    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    return result["messages"][-1].content


if __name__ == "__main__":
    gr.ChatInterface(chat).launch()
