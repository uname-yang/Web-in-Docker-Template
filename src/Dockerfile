FROM python:2.7

ADD . /code
WORKDIR /code

RUN pip install tornado redis

CMD python pagecount.py

EXPOSE 5000
