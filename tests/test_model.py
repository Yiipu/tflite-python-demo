import unittest
from PIL import Image
import numpy as np
from checkdown.models import tfliteModel
from checkdown import utils

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.model = tfliteModel(utils.get_model_path())

    def test_preprocess(self):
        # Create a test image
        image = Image.new('L', (28, 28))
        image_data = np.array(image)

        # Preprocess the image
        preprocessed_data = self.model.preprocess(image)

        # Check the shape and type of the preprocessed data
        self.assertEqual(preprocessed_data.shape, (1, 28, 28, 1))
        self.assertEqual(preprocessed_data.dtype, np.float32)

    def test_postprocess(self):
        # Create a test output data
        output_data = np.array([[0.1, 0.2, 0.7]])

        # Postprocess the output data
        predicted_label = self.model.postprocess(output_data)

        # Check the predicted label
        self.assertEqual(predicted_label, 'C')

    def test_predict(self):
        # Create a test input data
        input_data = Image.open('tests/input.png')

        # Predict the output
        output_data = self.model.predict(input_data)

        print(output_data)

        # Check the shape and type of the output data
        self.assertEqual(output_data, 'K')

if __name__ == '__main__':
    unittest.main()