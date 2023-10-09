FROM python:3.10-alpine

ENV PYENV=1
ENV PYENV=2
WORKDIR /django
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD python3 manage.py runserver