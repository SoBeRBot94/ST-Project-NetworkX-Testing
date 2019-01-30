FROM python:2.7-alpine

LABEL maintainer='SUDARSAN BHARGAVAN'

WORKDIR /BlackBoxTests
COPY ./networkxtest.py /BlackBoxTests/networkxtest.py
RUN apk add py-setuptools py-pip
RUN python2 -m pip install networkx pytest

ENV TERM xterm

CMD ["python", "/BlackBoxTests/networkxtest.py"]
