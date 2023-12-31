

from os import path, walk
from flask import Flask, render_template
from flask import request, redirect, session
from flask import jsonify, make_response

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
app.secret_key = 'very secret secret key'

# Set up the transcriber
scribe = WhisperTranscriber()

@app.route('/transcribe', methods=['POST', 'GET'])
def generate_transcript():
    result = ""
    if request.method == 'POST':
        file_loc, fname = recv_uploaded_audio(request, app.config["UPLOAD_FOLDER"])
        result = scribe.transcribe_audio_file(file_loc)

        print(result)

        if type(scribe) is WhisperTranscriber:
            data = scribe.process_results(result)
            session['w-transcript'] = data['words']
            print(data['words'])
            session['transcript'] = None
        else:
            session['transcript'] = result
            session['w-transcript'] = None

        # Save file information
        session['file_loc'] = file_loc
        session['filename'] = fname
    else:
        pass

    return redirect('/', code=307)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template("index.html", transcript=session.get('transcript'), whisper_transcript=session.get('w-transcript'), filename=session.get('filename'))

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
