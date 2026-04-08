from openai import OpenAI

#Configuro el cliente para que mire a mi propia mac (Localhost)
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" #Ollama no necesita API key, pero el cliente pide algo
)

try:
    response = client.chat.completions.create(
        model="phi3:latest",  #Asegurandome de haber hecho "ollama pull llama3" before  
        messages=[
            {"role": "system", "content": "You are a helpful assistant that tells fun facts"},
            {"role": "user", "content": "Tell me a fun fact"}
        ],

    )
    print("\nRespuesta desde Ollama (Local):")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error: Asegurate de que Ollama esté corriendo y que el modelo esté disponible")