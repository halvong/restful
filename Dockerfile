FROM python:3.6.5
LABEL maintainer="halvong@yahoo.com"

ENV PYTHONBUFFERED 1


RUN mkdir /app
WORKDIR /app
COPY . /app

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000