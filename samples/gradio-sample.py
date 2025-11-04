import gradio as gr

def chat_with_ai(message):
    # (Replace this with your model call)
    return f"You said: {message}"

chatbot = gr.ChatInterface(fn=chat_with_ai)
chatbot.launch()
