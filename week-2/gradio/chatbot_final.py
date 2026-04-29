import gradio as gr
from transformers import pipeline

# Usamos la versión de BLIP diseñada para Preguntas y Respuestas (VQA)
model_id = "Salesforce/blip-vqa-base"

print("Cargando motor de Preguntas y Respuestas... (Un par de segundos)")
# Creamos el pipeline específico para VQA
vqa_pipe = pipeline("visual-question-answering", model=model_id)

def responder(image, question):
    if image is None: return "Sube una imagen"
    if not question: return "Hazme una pregunta sobre la imagen"
    
    try:
        # El pipeline de VQA recibe imagen y pregunta por separado
        result = vqa_pipe(image, question)
        # El resultado suele ser una lista: [{'answer': 'un perro', 'score': ...}]
        return result[0]['answer']
    except Exception as e:
        return f"Error: {str(e)}"

# Interfaz con dos entradas (Imagen y Texto)
demo = gr.Interface(
    fn=responder,
    inputs=[
        gr.Image(type="pil", label="Sube tu imagen"),
        gr.Textbox(label="Tu pregunta (en inglés)", placeholder="Ej: What color is the car?")
    ],
    outputs=gr.Textbox(label="La IA responde:"),
    title="Chatbot Multimodal Interactivo",
    description="Ahora sí puedes preguntarme cosas sobre lo que ves en la imagen."
)

demo.launch(share=True)