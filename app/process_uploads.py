
"""
Process uploaded files by converting them to .wav for the transcriber.
"""

import os
from werkzeug.utils import secure_filename

# Uploads can only be certain extensions
ALLOWED_EXTENSIONS = {'wav', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'webm'}




def is_allowed_file_type(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def recv_uploaded_audio(request, dst_folder: str, key='audio_file') -> tuple:
    """
    Receive an uploaded file and check to see if it is valid. If it is, save it
    and return the path to where it got saved.
    """
    print(f"url: {request.url}\nfiles: {request.files}")

    new_file = ""
    safe_filename = ""
    if request.method == "POST":
        # If the file we are looking for exists in the request, then process it.
        if key in request.files:
            file = request.files[key]

            print(file.filename)

            # If the file name is blank, then there was no file uploaded.
            if file.filename == '':
                return ""
            
            # If the file is allowed and it exists, save it in temporary storage.
            if file and is_allowed_file_type(file.filename):
                print('valid file')
                safe_filename = secure_filename(file.filename)
                new_file = os.path.join(dst_folder, safe_filename)
                file.save(new_file)

        else:
            # Otherwise, there is no file of interest
            pass
    else:
        pass

    # Return the location of the file just saved and its short name.
    return new_file, safe_filename
    