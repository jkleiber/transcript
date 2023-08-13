
import whisper
from transcribers.transcriber import Transcriber

class WhisperTranscriber(Transcriber):

    def __init__(self) -> None:
        print("Loading Whisper...")
        self.model = whisper.load_model("base")
        print("Whisper initialized!")

    def transcribe_audio_file(self, file: str) -> str:
        result = self.model.transcribe(file)
        return result['text']

