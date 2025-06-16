FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./backend /app

# this command set in docker compose file so doesnt need to use again here
# CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ] 
