import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_LEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI"},
        {"role": "user", "content":"Give me 1 sentence in english"}
    ]
    )

print(response.choices[0].message.content)

