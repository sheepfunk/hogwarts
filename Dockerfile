FROM python:3.6

ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

ADD * /app/

WORKDIR /app

ENTRYPOINT ["/app/main.py"]