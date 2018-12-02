import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter

UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/")
@app.route("/index")
def index():
    for (dirpath, dirname, filenames) in os.walk(UPLOAD_FOLDER):
        print(filenames)
        #if(filenames != 'a.jpg' and filenames != 'b.jpg'):
            #os.remove(filenames[0])
    return render_template("upload.html")

@app.route('/upload', methods=[ 'POST'])
def upload_file():
    file = request.files['image']
    file_path = UPLOAD_FOLDER + file.filename
    if(file.filename != ' ' and allowed_file(file.filename)):
        file.save(file_path)
        img = Image.open('static/img/b.jpg')
        img = img.filter(ImageFilter.DETAIL)
        img = img.resize((600,600))
        img1 = Image.open('static/img/c.jpg')
        img1 = img1.filter(ImageFilter.DETAIL)
        img1 = img1.resize((600,600))
        img2 = Image.open(file_path)
        img2 = img2.filter(ImageFilter.DETAIL)
        img2 = img2.resize((600,600))
        r = []
        g = []
        b = []
        red, green, blue = img.split()
        r.append(red)
        g.append(green)
        b.append(blue)
        red, green, blue = img1.split()
        r.append(red)
        g.append(green)
        b.append(blue)
        red, green, blue = img2.split()
        r.append(red)
        g.append(green)
        b.append(blue)
        images = []
        count = 1
        for i in r:
            for j in  g:
                for k in b:
                    path = 'static/img/'+ str(count)+'.jpg'
                    Image.merge("RGB", (i,j,k)).save(path)
                    images.append(path)
                    count += 1;
    return render_template('images.html', images = images)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True)
