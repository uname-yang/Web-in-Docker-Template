FROM python:2.7

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD python pagecount.py

EXPOSE 5000
