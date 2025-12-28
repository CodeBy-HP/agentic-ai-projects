from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

structured_llm=llm.with_structured_output(AgentResponse)

react_prompt = hub.pull("hwchase17/react")

react_prompt_with_format_instructions=PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input","agent_scratchpad","tool_names"]
).partial(format_instructions="")

agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_format_instructions)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

extract_output=RunnableLambda(lambda x:x["output"])
chain = agent_executor|extract_output|structured_llm


def main():
    print("Hello from langchain-projects!")
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bhopal on linkedin and list their details",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
