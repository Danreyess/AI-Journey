import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": """
                You are a professional English Teacher.
                Your goal is to help a student reach B2 level. 
            """
        },
        {
            "role": "user",
            "content": "I wants to know how to improve my speaking"
        }
    ],
    temperature=0.5
)

print(response.choices[0].message.content)