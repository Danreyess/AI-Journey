import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

local = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
claude = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_api(client,model,question):
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role":"user", "content":question}
        ]
    )
    return response.choices[0].message.content

#Calling OpenAI model
v1 = call_api(local, "phi3:latest", "Tell me a fun fact about beavers")
print(v1)
