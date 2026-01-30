from gtts import gTTS
import tempfile

class TextToSpeechService:
    def __init__(self, lang="pt"):
        self.lang = lang

    def syntethize(self, text: str) -> str:
        tts = gTTS(text=text, lang=self.lang)

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp_audio:
            tts.write_to_fp(temp_audio)
            audio_path = temp_audio.name
        return audio_path