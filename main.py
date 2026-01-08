from dotenv import load_dotenv
import os

load_dotenv()

from rich.console import Console
from openai import AzureOpenAI
from todo import TOOLS, handle_tool_calls, todos, completed, show

client = AzureOpenAI(azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))


def loop(messages):
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
    show(response.choices[0].message.content)


system_message = """
You are given a problem to solve, by using your todo tools to plan a list of steps, then carrying out each step in turn.
Now use the todo list tools, create a plan, carry out the steps, and reply with the solution.
If any quantity isn't provided in the question, then include a step to come up with a reasonable estimate.
Provide your solution in Rich console markup without code blocks.
Do not ask the user questions or clarification; respond only with the answer after using your tools.
"""

if __name__ == "__main__":
    todos.clear()
    completed.clear()
    user_message = """"
    A train leaves Boston at 2:00 pm traveling 60 mph.
    Another train leaves New York at 3:00 pm traveling 80 mph toward Boston.
    When do they meet?
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    loop(messages)
