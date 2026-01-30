import os
from dotenv import load_dotenv
import google.generativeai as genai

class AiAssistant:
    def __init__(self, model="gemini-2.5-flash"):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(model)

    def _format_messages_to_gemini(self, chat_history):
        formatted = []

        for msg in chat_history:
            role = "model" if msg["role"] == "assistant" else "user"
            formatted.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })
        return formatted
    
    def ask(self, messages: list[dict]) -> str:
        chat = self.model.start_chat(
            history=self._format_messages_to_gemini(messages)
        )

        response = chat.send_message(messages[-1]["content"])
        return response.text