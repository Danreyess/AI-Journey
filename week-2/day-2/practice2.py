from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are OpenAI"},
        {"role": "user", "content": "How long time does it take me to be a jr in LLM?"}
    ]
)

print(response.choices[0].message.content)