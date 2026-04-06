from config import client

# Ya puedes usar el cliente directamente
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a profesional English Teacher"},
              {"role": "user", "content": "Hi, I want to improve my english"},
    ],
    temperature=0.5,
)
print("\nRespuesta de la AI:")
print(response.choices[0].message.content)