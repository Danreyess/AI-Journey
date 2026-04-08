#Create an OpenAI client
from config import client
from openai import OpenAI

openai = OpenAI()

response = openai.chat.completions.create(model ="gpt-4o-mini", messages=[{"role": "user", "content": "Tell me a fun fact"}])
print(response.choices[0].message.content)