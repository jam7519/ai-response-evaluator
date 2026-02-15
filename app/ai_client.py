import os
from openai import OpenAI

client = OpenAI(api_key="PASTE YOUR API KEY HERE")


def ask_ai(question: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )

    return response.output_text
