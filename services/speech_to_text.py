import whisper

class WhisperLocalSTT():
    def __init__(self, model_name="small"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path) -> str:
        result = self.model.transcribe(audio_path)
        return result["text"]