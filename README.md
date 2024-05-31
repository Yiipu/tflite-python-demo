# TensorFlow Lite Model Deployment Demo

This project demonstrates how to deploy a TensorFlow Lite model using both a command line interface (CLI) and a web API.

## Installation

First, clone this repository:

```bash
git clone https://github.com/yiipu/tflite-python-demo.git
cd tflite-python-demo
```

Then, install the package:

```bash
pip install .
```

## Usage

### CLI

```bash
checkdown --input tests/input.png
```

### API

To start the API server, run the following command:

```bash
cd checkdown
python api.py
```

The API server will start on `http://localhost:5000`. To use the API, send a POST request to `http://localhost:5000/predict` with your input data.

example:
```bash
curl -X POST -F "file=@tests/input.png" http://localhost:5000/predict
```

> note that you should replace `tests/input.png` with your own image file.

### Docker

[TODO]