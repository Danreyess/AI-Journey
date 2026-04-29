from transformers import pipeline
from PIL import Image

# Esto usará los archivos que YA descargaste
pipe = pipeline("image-to-text", model="llava-hf/llava-1.5-7b-hf", device_map="auto")

# Cambia esto por la ruta de cualquier imagen que tengas en tu escritorio
image_path = "/Users/dani/Desktop/test.jpg" 
image = Image.open(image_path)

prompt = "USER: <image>\nWhat is in this image?\nASSISTANT:"
outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 50})

print("\n--- RESPUESTA DE LA IA ---")
print(outputs[0]["generated_text"].split("ASSISTANT:")[-1])