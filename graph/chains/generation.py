from dotenv import load_dotenv
from langsmith import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
import os

load_dotenv()
llm = AzureChatOpenAI(
    temperature=0,
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

client = Client()
prompt = client.pull_prompt("rlm/rag-prompt", include_model=True)

generation_chain = prompt | llm | StrOutputParser()
