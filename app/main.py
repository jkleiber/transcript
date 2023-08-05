

from os import path, walk
from flask import Flask, render_template, send_from_directory
from flask import request, abort, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def poll_landing_page():
    return render_template("index.html")

if __name__ == "__main__":
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
