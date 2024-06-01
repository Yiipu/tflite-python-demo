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
gunicorn -w 4 checkdown.api:app
```

The API server will start on `http://localhost:8000`. To use the API, send a POST request to `http://localhost:8000/predict` with your input data.

example:
```bash
curl -X POST -F "file=@tests/input.png" http://localhost:8000/predict
```

> note that you should replace `tests/input.png` with your own image file.

### Docker

To run the API server in a Docker container, first build the image:

```bash
docker build -t checkdown -f docker/api.dockerfile .
```

Then, run the container:

```bash
docker run -p 4000:8000 -it checkdown
```

> note that you can replace `4000` with any port you like. this will be the host port that the container will be mapped to.

you can also use the cli in the docker container:

```bash
docker run -it checkdown bash
checkdown --input tests/input.png
```