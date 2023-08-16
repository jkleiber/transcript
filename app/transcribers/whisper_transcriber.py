
import whisper_timestamped as whisper
from transcribers.transcriber import Transcriber


class WhisperTranscriber(Transcriber):

    def __init__(self) -> None:
        print("Loading Whisper...")
        self.model = whisper.load_model("base", device='cpu')
        print("Whisper initialized!")

    def transcribe_audio_file(self, file: str) -> str:
        audio = whisper.load_audio(file)
        result = whisper.transcribe(self.model, audio, language='en')
        return result

    def process_results(self, results: dict) -> dict:
        word_data = []
        phrase_data = []

        # Compile phrases
        for seg in results['segments']:
            # Save the phrase.
            phrase = {
                'text': seg['text'],
                'id': seg['id'],
                'confidence': seg['confidence'],
                'start': seg['start'],
                'end': seg['end']
            }
            phrase_data.append(phrase)

            # Compile words
            for word in seg['words']:
                word = {
                    'text': word['text'],
                    'confidence': word['confidence'],
                    'start': word['start'],
                    'end': word['end']
                }
                word_data.append(word)

        # Return both words and phrases as a dictionary
        data = {
            'phrases': phrase_data,
            'words': word_data
        }
        return data
