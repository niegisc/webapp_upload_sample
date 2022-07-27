import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

photolist = []
photo_file = open('photolist.txt', 'a')
photo_file.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    image = request.files['photo']
    path = os.path.join('uploads',image.filename)
    image.save(path)
    photolist.append(image.filename)
    return render_template('index.html', filename=image.filename, images=photolist)

@app.route('/photos/<filename>')
def get_file(filename):
    return send_from_directory('uploads', filename)

app.run()
