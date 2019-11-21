FROM debian:latest

COPY ./py-base/requirements.txt ./

RUN apt-get update && \
apt-get -y install python3 python3-pip git && \
pip3 install -r requirements.txt && \
ln -sf /usr/bin/python3 /usr/bin/python