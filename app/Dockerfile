# Dockerfile, Image, Container
FROM python:3.8.2

WORKDIR /case-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]