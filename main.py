import gradio as gr
import requests

API_KEY = "sk_api_49963a85a4e15093c348640290231870c321217215504d304dd2cb87d8fface8"

def generate_voice(text, image):
    """Send text to Orator API and return Urdu voice + display image."""
    if not text.strip():
        return "⚠️ Please enter some text.", None

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"text": text, "language": "ur"}
    try:
        # Example request (replace with your real Orator endpoint)
        response = requests.post("https://api.orator.ai/generate", json=payload, headers=headers)
        if response.status_code == 200:
            audio_url = response.json().get("audio_url")
            return f"✅ Urdu voice generated successfully!", audio_url
        else:
            return f"❌ Error: {response.text}", None
    except Exception as e:
        return f"⚠️ Connection failed: {e}", None


with gr.Blocks(title="🎙️ Urdu AI Orator") as app:
    gr.Markdown("# 🎧 Urdu AI Orator\n### Convert your text into Urdu voice instantly!")
    with gr.Row():
        image = gr.Image(label="Upload App Picture (optional)")
    text = gr.Textbox(label="Enter Urdu text", placeholder="Type your script here...")
    btn = gr.Button("🎤 Generate Voice")
    output_text = gr.Textbox(label="Status")
    audio = gr.Audio(label="Generated Voice", interactive=False)

    btn.click(generate_voice, inputs=[text, image], outputs=[output_text, audio])

app.launch()
