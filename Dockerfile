FROM python:3.6

ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

ADD src/* /app/
RUN ln -s /app/secrets/secrets.py /app/secrets.py

WORKDIR /app

ENTRYPOINT ["/app/main.py"]