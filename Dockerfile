FROM python:3.7.4
LABEL maintainer="halvong@yahoo.com"

ENV PYTHONBUFFERED 1


RUN mkdir /app
WORKDIR /app
COPY . /app

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the image as a non-root user
RUN adduser --disabled-login --gecos '' tom
USER tom

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi
CMD python manage.py runserver 0.0.0.0:8000
