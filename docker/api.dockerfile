FROM python:3.9.19
WORKDIR /app
ADD . /app
RUN pip install .[api]
EXPOSE 8000
CMD ["gunicorn", "-w 4", "checkdown.api:app"]