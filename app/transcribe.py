
import json
import subprocess
from vosk import Model, KaldiRecognizer
SAMPLE_RATE = 16000

# Load up the vosk model.
model = Model(lang="en-us")
rec = KaldiRecognizer(model, SAMPLE_RATE)

def transcribe_audio_file(file: str) -> str:
    # Convert the input file in a subprocess and do the speech recognition.
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                            file,
                            "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                            stdout=subprocess.PIPE) as process:
        while True:
            data = process.stdout.read(4000)
            if len(data) == 0:
                # No data left to process.
                break
            
            # Print status.
            rec.AcceptWaveform(data)

    # Return the final result
    result_json = json.loads(rec.FinalResult())
    return result_json['text']
