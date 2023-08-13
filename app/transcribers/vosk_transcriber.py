
import json
import subprocess
from transcribers.transcriber import Transcriber

# Third party imports
from vosk import Model, KaldiRecognizer


class VoskTranscriber(Transcriber):

    SAMPLE_RATE = 16000

    def __init__(self) -> None:
        # Load up the vosk model.
        self.model = Model(lang="en-us")
        self.rec = KaldiRecognizer(self.model, self.SAMPLE_RATE)

    def transcribe_audio_file(self, file: str) -> str:
        # Convert the input file in a subprocess and do the speech recognition.
        with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                               file,
                               "-ar", str(self.SAMPLE_RATE), "-ac", "1", "-f", "s16le", "-"],
                              stdout=subprocess.PIPE) as process:
            while True:
                data = process.stdout.read(4000)
                if len(data) == 0:
                    # No data left to process.
                    break

                # Print status.
                self.rec.AcceptWaveform(data)

        # Return the final result
        result_json = json.loads(self.rec.FinalResult())
        return result_json['text']
