from dotenv import load_dotenv
import os
from openai import AzureOpenAI
from pypdf import PdfReader
import requests
from tools import handle_tool_calls, TOOLS

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

SYSTEM_PROMPT = f"You are acting as {NAME}. You are answering questions on {NAME}'s website, \
particularly questions related to {NAME}'s career, background, skills and experience. \
Your responsibility is to represent {NAME} for interactions on the website as faithfully as possible. \
You are given a summary of {NAME}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

SYSTEM_PROMPT += f"\n\n## Summary:\n{SUMMARY}\n\n## LinkedIn Profile:\n{LINKEDIN}\n\n"
SYSTEM_PROMPT += f"With this context, please chat with the user, always staying in character as {NAME}."


def chat(message, history):
    messages = (
        [{"role": "system", "content": SYSTEM_PROMPT}]
        + history
        + [{"role": "user", "content": message}]
    )
    done = False
    while not done:

        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages, tools=TOOLS
        )

        finish_reason = response.choices[0].finish_reason

        if finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
        else:
            done = True
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
