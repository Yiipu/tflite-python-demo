from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from checkdown.models import tfliteModel
from checkdown.utils import get_model_path

app = Flask(__name__)
model = tfliteModel(get_model_path())

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(BytesIO(file.read()))
    prediction = model.predict(image)
    return jsonify({'predict': prediction})


if __name__ == '__main__':
    app.run()