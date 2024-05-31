FROM python:3.10-slim-buster
WORKDIR /app
ADD . /app

RUN pip install -e .[api]

EXPOSE 5000

CMD ["python", "checkdown/api.py"]