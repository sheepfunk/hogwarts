FROM python:3.6

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/secrets/hogwarts-bot-credentials.json
ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

ADD src/* /app/
# You need this to run it locally via `docker run -it sheepfunk/hogwarts-bot:latest`
#ADD secrets.py /app/secrets/
#ADD hogwarts-bot-credentials.json /app/secrets/
RUN ln -s /app/secrets/secrets.py /app/secrets.py

WORKDIR /app

ENTRYPOINT ["/app/main.py"]