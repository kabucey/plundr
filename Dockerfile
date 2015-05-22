FROM python:3.4
ADD . /code
WORKDIR /code
ENV BOOTY 42
RUN pip install -r requirements.txt
