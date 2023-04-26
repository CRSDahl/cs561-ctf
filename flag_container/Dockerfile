FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    net-tools \
    ncat \
    nmap \
    iproute2 \
    openssh-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password ctfuser && echo 'ctfuser:ctfuser' | chpasswd
RUN adduser --disabled-password admin

COPY id_rsa.pub /home/admin/.ssh/authorized_keys

COPY flag.txt /home/admin/flag.txt
RUN chown admin:admin /home/admin/flag.txt
RUN chmod 400 /home/admin/flag.txt
RUN ln -s /home/admin/flag.txt /home/ctfuser/flag.txt

RUN echo "AllowUsers admin@192.168.0.4 ctfuser" > /etc/ssh/sshd_config

ENTRYPOINT service ssh start && tail -f /dev/null