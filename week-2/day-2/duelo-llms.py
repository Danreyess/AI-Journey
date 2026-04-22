import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Configurar el cliente 
cliente_nube = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

cliente_local = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def obtener_respuesta(cliente, modelo,pregunta):
    try:
        response = cliente.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": pregunta}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

#Configuracion del duelo 
pregunta_usuario = "Dame una receta rapida de 3 pasos para cocinar papas."

print("Inicializando comparacion...")

#Llamada de OpenAI
print("Respuesta OPENAI (GPT-4o-mini)")
res_nube = obtener_respuesta(cliente_nube, "gpt-4o-mini", pregunta_usuario)
print(res_nube)

#Llamada de Ollama
print("Respuesta de ollama")
res_local = obtener_respuesta(cliente_local, "phi3:latest", pregunta_usuario)
print(res_local)