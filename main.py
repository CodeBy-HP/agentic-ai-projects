from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from schemas import AgentResponse

tools = [TavilySearch()]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ToolStrategy(AgentResponse),
    system_prompt="You are a helpful assistant that searches for information and provides structured responses with sources."
)


def main():
    print("Hello from langchain-projects!")
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "search for 3 job postings for an ai engineer using langchain in the bhopal on linkedin and list their details"}
            ]
        }
    )
    print(result["structured_response"])


if __name__ == "__main__":
    main()
