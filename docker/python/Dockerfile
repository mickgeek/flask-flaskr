FROM python:3.8.0-buster

# Install required libraries
RUN apt-get update -y \
    && apt-get -y --no-install-recommends install \
        python3-venv \
        python3-pip \
        sqlite3 \
        # Python dependencies
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./flaskr/ /home/flaskr/
COPY ./start.sh /home/

WORKDIR /home/

RUN python3 -m venv venv \
    && pip install --upgrade pip \
    && pip install flask \
    && pip install flask-migrate \
    && pip install flask-script \
    && pip install flask-wtf \
    && pip install psycopg2 \
    && pip install gunicorn

ENV FLASK_APP=${FLASK_APP}
ENV FLASK_ENV=${FLASK_ENV}

RUN chmod +x /home/start.sh

CMD ["/bin/bash", "/home/start.sh"]
