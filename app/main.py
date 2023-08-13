

from os import path, walk
from flask import Flask, render_template, send_from_directory
from flask import request, abort, url_for

from process_uploads import recv_uploaded_audio
# from transcribers.vosk_transcriber import VoskTranscriber
from transcribers.whisper_transcriber import WhisperTranscriber

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Max upload size: 25 MB
app.config['MAX_CONTENT_LENGTH'] = 25 * 1000 * 1000

app.config['UPLOAD_FOLDER'] = "/tmp"

# Set up the transcriber
scribe = WhisperTranscriber()

@app.route('/transcribe', methods=['POST', 'GET'])
def generate_transcript():
    result = ""
    if request.method == 'POST':
        file_loc = recv_uploaded_audio(request, app.config["UPLOAD_FOLDER"])
        result = scribe.transcribe_audio_file(file_loc)
        # result = transcribe_audio_file(file_loc)

        print(f"Result: {result}")

    return render_template("index.html", transcript_results=result)

@app.route('/', methods=['GET', 'POST'])
def poll_landing_page():
    return render_template("index.html")

if __name__ == "__main__":
    print("Initializing Transcript...")

    # Hot reloading for when static files change.
    # Don't include static/data, since those files should be explicitly loaded and saved anyway.
    extra_dirs = ['static/css', 'static/components', 'static/doc',
                  'static/img', 'static/js', 'templates']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)

    app.run(extra_files=extra_files, host='0.0.0.0', port=5001)
