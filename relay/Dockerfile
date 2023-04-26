FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    openssh-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN adduser --disabled-password admin

COPY id_rsa.pub /home/admin/.ssh/authorized_keys

WORKDIR /app
ENTRYPOINT service ssh start && tail -f /dev/null