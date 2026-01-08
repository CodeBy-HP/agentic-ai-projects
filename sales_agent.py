from agents import Agent, set_default_openai_client, function_tool
from openai import AsyncAzureOpenAI
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

load_dotenv()


client = AsyncAzureOpenAI(
    api_version="2025-03-01-preview",
)
set_default_openai_client(client)
AZURE_MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT")


instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

instructions3 = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."


sales_agent1 = Agent(
    name="Professional Sales Agent", instructions=instructions1, model=AZURE_MODEL
)

sales_agent2 = Agent(
    name="Engaging Sales Agent", instructions=instructions2, model=AZURE_MODEL
)

sales_agent3 = Agent(
    name="Busy Sales Agent", instructions=instructions3, model=AZURE_MODEL
)


@function_tool
def send_email(body: str):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("code.by.hp@gmail.com")
    to_email = To("harshdousab372004@gmail.com")
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, "Test email", content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


tool1 = sales_agent1.as_tool(
    tool_name="professional_agent",
    tool_description="Generate a professional, serious sales email draft.",
)

tool2 = sales_agent2.as_tool(
    tool_name="engaging_agent",
    tool_description="Generate a witty, humorous sales email draft.",
)

tool3 = sales_agent3.as_tool(
    tool_name="concise_agent",
    tool_description="Generate a short, concise sales email draft.",
)

TOOLS = [tool1, tool2, tool3, send_email]

instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email.

Follow this workflow STRICTLY:

1. **Draft Generation**: 
   - Call `professional_agent`, `engaging_agent`, and `concise_agent` to get three distinct drafts.
   - **CRITICAL**: Once you have received the output from these three tools, **DO NOT call them again**. You have the drafts. Move immediately to step 2.

2. **Evaluation**: 
   - Review the text returned by the tools in Step 1.
   - Select the single best draft based on your judgment.

3. **Execution**:
   - Call the `send_email` tool with the body of the winning draft.
   - After sending, terminate the process.

**Constraints:**
- Do not add your own commentary to the email body when sending.
- Never loop back to Step 1 after you have the drafts.
"""

sales_manager = Agent(
    name="Sales Manager", instructions=instructions, tools=TOOLS, model=AZURE_MODEL
)
