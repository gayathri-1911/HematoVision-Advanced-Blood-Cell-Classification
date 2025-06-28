from flask import Flask, request, render_template, redirect
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import base64
import os
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

app = Flask(__name__)

# Load the model
model = load_model("blood_cell_classifier.h5")

# Define class labels
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']

# Prediction function
def predict_image_class(image_path, model):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_preprocessed = preprocess_input(img_resized.reshape((1, 224, 224, 3)))
    predictions = model.predict(img_preprocessed)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_idx]
    return predicted_class_label, img_rgb

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If no file was selected
        if file.filename == '':
            return redirect(request.url)
        
        # Save the uploaded file temporarily
        temp_path = os.path.join('static', 'temp.jpg')
        os.makedirs('static', exist_ok=True)
        file.save(temp_path)
        
        # Make prediction
        class_label, img = predict_image_class(temp_path, model)
        
        # Convert image to base64 for displaying in HTML
        _, buffer = cv2.imencode('.jpg', img)
        img_data = base64.b64encode(buffer).decode('utf-8')
        
        # Return the result page
        return render_template('result.html', class_label=class_label, img_data=img_data)
    
    # GET request - show the upload form
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
