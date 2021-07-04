FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN mkdir /code
WORKDIR /code

COPY ./requirements /requirements

RUN pip3 install -r /requirements/local.txt

ADD . /code/

COPY docker-files/web/run_web.sh /start-run_web.sh
RUN sed -i 's/\r//' /start-run_web.sh
RUN chmod +x /start-run_web.sh

# create unprivileged user
RUN adduser --disabled-password --gecos '' deploy