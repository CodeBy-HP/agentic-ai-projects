from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from pypdf import PdfReader

load_dotenv()

client = AzureOpenAI(azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))

if os.path.exists("static/profile.pdf"):
    reader = PdfReader("static/profile.pdf")
    LINKEDIN = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            LINKEDIN += text
else:
    LINKEDIN = "Profile PDF not found."

if os.path.exists("static/summary.txt"):
    with open("static/summary.txt", "r", encoding="utf-8") as f:
        SUMMARY = f.read()
else:
    SUMMARY = "Summary text not found."

NAME = "Harsh Patel"

SYSTEM_PROMPT = f"""You are acting as {NAME}. Answer questions on {NAME}'s website related to their career, skills, and experience.
Represent {NAME} faithfully using the provided context. Be professional and engaging.
If you don't know the answer, say so.
## Summary:
{SUMMARY}
## LinkedIn Profile:
{LINKEDIN}
With this context, chat with the user, staying in character as {NAME}."""


def chat(query, history):
    # History is automatically handled by Gradio.
    # History -> [{'role': 'user', 'content': 'hi'}, {'role': 'assistant', 'content': 'hello'}]
    messages = (
        [{"role": "system", "content": SYSTEM_PROMPT}]
        + history
        + [{"role": "user", "content": query}]
    )

    response = client.chat.completions.create(
        model=str(os.getenv("AZURE_OPENAI_DEPLOYMENT")), messages=messages
    )
    return response.choices[0].message.content


def main():
    from gradio.chat_interface import ChatInterface

    ChatInterface(
        fn=chat,
        title=f"Chat with {NAME}",
        description="Ask me anything about my professional background.",
    ).launch()


if __name__ == "__main__":
    main()
