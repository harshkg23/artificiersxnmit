from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, UnidentifiedImageError
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'static/img'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = load_model('model.h5')  # Replace with the actual path to your model

# Image parameters
img_height, img_width = 224, 224

def preprocess_image(img_path):
    try:
        img = Image.open(img_path)
        img = img.resize((img_height, img_width))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        if img.shape == (1, img_height, img_width, 3):  # Ensure the image has the correct shape
            print("image returned")
            return img
        else:
            return None
    except UnidentifiedImageError:
        return None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            img = preprocess_image(filepath)
            if img is not None:
                prediction = model.predict(img)
                result = "Malignant" if prediction[0][0] > 0.5 else "Benign"
                return render_template('result.html', result=result, filepath=filepath)
            else:
                return "Error: Unable to process the image. Make sure it is in the correct format."
    return render_template('upload.html')

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='img/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)
