from openai import OpenAI
from pyexpat.errors import messages


class Summarizer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def summarize(self, content):
        completition = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Sumiraj sledeci tekst u 2-3 recenice: {content}"}
            ]
        )

        return completition.choices[0].message.content.strip()