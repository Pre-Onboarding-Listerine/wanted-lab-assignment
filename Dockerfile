FROM python:3.9

WORKDIR /app
COPY . /app

# ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt
