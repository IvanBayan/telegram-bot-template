FROM python:3.7-stretch

RUN mkdir -p /app/data
ADD . /app/
WORKDIR /app

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install libzbar0 -y
RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENV DB_URI sqlite:////app/data/db.sqlite
RUN python3 -m bot setup-database

ENV MODE polling
CMD python3 -m bot start-$MODE
