import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np

class tfliteModel:
    def __init__(self, model_path):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

    def preprocess(self, input_data):
        # 将图片转化为(28,28)的灰度图
        input_data = input_data.convert('L').resize((28, 28))
        input_data = np.array(input_data).reshape(1, 28, 28, 1)
        input_data = input_data/255.0
        return input_data.astype(np.float32)

    def postprocess(self, output_data):
        map = {i: chr(i + ord('A')) for i in range(26)}
        return map[np.argmax(output_data, axis=1)[0]]

    def predict(self, input_data):
        input_data = self.preprocess(input_data)
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        self.interpreter.set_tensor(input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(output_details[0]['index'])
        return self.postprocess(output_data)