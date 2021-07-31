from flask import Flask, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

import json
import os

from readcsv import *

UPLOAD_FOLDER = 'uploads'
# create empty upload foler if not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
CORS(app) # enabling CORS

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload_files', methods=['GET','POST'])
def upload_files():
    print("-------upload files upload files-----------")
    result = "Successful"
    if request.method == 'POST':
        # check if the post has request has the file
        if 'file1' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file1 = request.files['file1']
        file2 = request.files['file2']
        print("file 1", file1)
        print("file 2", file2)

        if file1 and file2:
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            
            print("filename1: ", filename1)
            print("filename2: ", filename2)

            file1.save(os.path.join(UPLOAD_FOLDER, filename1))
            file2.save(os.path.join(UPLOAD_FOLDER, filename2))

            result = execute(os.path.join(UPLOAD_FOLDER, filename1), os.path.join(UPLOAD_FOLDER, filename2))
            print("------result-------", result)

            return result

    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
