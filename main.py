"""
1 - Criar interface básica com o streamlit;
2 - Receber o áudio e transcrever;
3 - Integrar API do Gemini;
4 - Converter resposta em texto usando gTTS (Google Text To Speach)
"""

import streamlit as st
import tempfile
from services.speech_to_text import WhisperLocalSTT


class App:
    def __init__(self, **services):
        self.stt = services['speech_to_text']
        self.llm = services['large_language_model']
        self.tts = services['talk_to_speech']

    def run(self):
        st.title("VoxFlow 🎙️🤖")

        # ---------- Session State ----------
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "transcription" not in st.session_state:
            st.session_state.transcription = None

        if "audio_key" not in st.session_state:
            st.session_state.audio_key = 0

        # ---------- Histórico ----------
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # ---------- Áudio ----------
        audio_value = st.audio_input(
            "Grave sua mensagem:",
            key=f"audio_{st.session_state.audio_key}"
        )

        if audio_value and st.session_state.transcription is None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
                temp.write(audio_value.read())
                temp.flush()
                audio_path = temp.name

            st.session_state.transcription = self.stt.transcribe(audio_path)

        # ---------- Texto + Envio (SÓ SE HOUVER ÁUDIO) ----------
        if st.session_state.transcription:
            user_text = st.text_area(
                "Texto para envio",
                value=st.session_state.transcription,
                height=100
            )

            if st.button("Enviar") and user_text.strip():
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_text
                })

                # Aqui entra futuramente:
                # response = self.llm.ask(user_text)

                # ---------- Reset ----------
                st.session_state.transcription = None
                st.session_state.audio_key += 1  # limpa audio_input
                st.rerun()


if __name__ == "__main__":
    stt = WhisperLocalSTT()

    app = App(
        speech_to_text=stt,
        large_language_model=None,
        talk_to_speech=None
    )

    app.run()
