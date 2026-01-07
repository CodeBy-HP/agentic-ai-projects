from optparse import Option
from dotenv import load_dotenv
import os

load_dotenv(override=True)

from typing import Optional
from openai import AzureOpenAI

client = AzureOpenAI(azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))


def generate_story(topic: str) -> Optional[str]:
    response = client.chat.completions.create(
        model=str(os.getenv("AZURE_OPENAI_DEPLOYMENT")),
        messages=[
            {
                "role": "user",
                "content": f"Write a short story about {topic} in 500 words",
            }
        ],
    )
    return response.choices[0].message.content


def translate(story: str) -> Optional[str]:
    response = client.chat.completions.create(
        model=str(os.getenv("AZURE_OPENAI_DEPLOYMENT")),
        messages=[
            {"role": "user", "content": f"Translate the given story {story} to Hindi."}
        ],
    )
    return response.choices[0].message.content


def summarize(story: str) -> Optional[str]:
    response = client.chat.completions.create(
        model=str(os.getenv("AZURE_OPENAI_DEPLOYMENT")),
        messages=[
            {
                "role": "user",
                "content": f"Summarize the given story {story} in 2 lines in Hindi",
            }
        ],
    )
    return response.choices[0].message.content


def main():
    print("Hello from projects!")
    print("Generating the Story")
    story = generate_story(topic="Alexander the Great")
    print(f"Generate Story \n {story}")
    print("Translating the story to Hindi")
    translated_story = translate(story=story)
    print(f"Translated Story \n {translated_story} ")
    print("Summarizing the story")
    summarized_story = summarize(story=translated_story)

    print(summarized_story)


if __name__ == "__main__":
    main()
