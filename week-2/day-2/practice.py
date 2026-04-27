#Practice duelo LLM
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

#Creacion de clientes
client_nube = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

client_local = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

#definir la funcion
def practicando(cliente,modelo,pregunta):
    response = cliente.chat.completions.create(
        model = modelo,
        messages = [
            {"role": "system", "content": "You are an helpful AI"},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message.content

#llamando clientes
print("Response OPENAI")
res_nube = practicando(client_nube, "gpt-4o-mini", "Give me a 3 sentences in english")
print(res_nube)

print("Response Ollama")
res_local = practicando(client_local, "phi3:latest", "Give me a 3 sentences in english ")8
print(res_local)