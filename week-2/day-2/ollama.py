import os
from pydoc import cli 
from openai import OpenAI

#Configurando cliente para que corra con ollama 
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" #Ollama no necesita API Key pero el cliente pide algo 
)

response = client.chat.completions.create(
    model="phi3:latest",
    messages=[
        {"role": "system", "content": "You are a helpful AI model"},
        {"role": "user", "content": "Tell me how to get my first job as a AI Engineer"}
    ]
)
print("Respuesta desde ollama (Local):")
print(response.choices[0].message.content)
