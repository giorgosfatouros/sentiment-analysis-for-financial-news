# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /sentiment-analysis-for-financial-news

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

COPY . .
ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]