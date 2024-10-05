import os
from openai import OpenAI

chatGPT_key = os.environ["chatGPT_key"]

client = OpenAI(api_key=chatGPT_key)

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Return only the the name of the city pressent in the following text, if none retun [null], the text is[locuiesc in dolhasca]",
    }],
    model="gpt-3.5-turbo",
)
response_text = response.choices[0].message.content
print(response_text)