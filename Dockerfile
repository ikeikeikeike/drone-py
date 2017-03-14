FROM python:3.5.1-alpine

RUN echo "ipv6" >> /etc/modules

ADD repositories /etc/apk/repositories
RUN apk --update add openssl
