import os
from openai import OpenAI

class GPT:
    def __init__(self):
        self.chatGPT_key = os.environ["chatGPT_key"]
        self.client = OpenAI(api_key=self.chatGPT_key)

    def get_response(self, content):
        response = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": content,
            }],
            model="gpt-3.5-turbo",
        )

        response_text = response.choices[0].message.content

        return response_text