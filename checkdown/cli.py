import argparse
from checkdown.models import tfliteModel
from PIL import Image

def main(args):
    model = tfliteModel(args.model)
    image = Image.open(args.input)
    result = model.predict(image)
    print(result)

if __name__ == '__main__':
    main()

