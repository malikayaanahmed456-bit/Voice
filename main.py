# ==========================================================
# 🎙️ Urdu AI Orator — Lightweight Android App (Kivy)
# ==========================================================
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

# 🔑 Replace with your Orator API key
API_KEY = "sk_api_49963a85a4e15093c348640290231870c321217215504d304dd2cb87d8fface8"
API_URL = "https://api.orator.com/v1/generate"

class UrduOratorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.add_widget(Label(text="🎙️ Urdu AI Orator", font_size='24sp', size_hint=(1,0.15)))
        self.text_input = TextInput(hint_text="Enter Urdu text...", size_hint=(1,0.25))
        self.add_widget(self.text_input)
        self.btn = Button(text="Generate Voice", size_hint=(1,0.2))
        self.btn.bind(on_press=self.generate_voice)
        self.add_widget(self.btn)
        self.result = Label(text="", font_size='18sp', size_hint=(1,0.2))
        self.add_widget(self.result)

    def generate_voice(self, instance):
        text = self.text_input.text.strip()
        if not text:
            self.result.text = "⚠️ Please enter Urdu text first!"
            return
        try:
            headers = {"Authorization": f"Bearer {API_KEY}"}
            data = {"text": text, "language": "ur"}
            r = requests.post(API_URL, headers=headers, json=data)
            if r.status_code == 200:
                self.result.text = "✅ Voice generated successfully!"
            else:
                self.result.text = "❌ API Error: " + str(r.text)
        except Exception as e:
            self.result.text = "⚠️ Error: " + str(e)

class UrduAIOratorApp(App):
    def build(self):
        return UrduOratorLayout()

if __name__ == "__main__":
    UrduAIOratorApp().run()
