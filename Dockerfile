FROM python:3.5.1-alpine

RUN echo "ipv6" >> /etc/modules
RUN
    echo "@edge-testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
    echo "@edge-community http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
    apk update && apk upgrade
    apk add alpine-sdk wget postgresql-dev mercurial libffi-dev libxml2-dev libxslt-dev libjpeg-turbo libjpeg-turbo-dev libzip-dev@edge-community openssl
    apk add zlib-dev libpng-dev fontconfig ttf-dejavu ttf-droid-nonlatin ttf-liberation ttf-ubuntu-font-family poppler-utils waitforit@edge-testing nodejs-lts
    pip install --upgrade virtualenv pip


# Copy pip config
COPY .common/pip.conf /root/.config/pip/pip.conf

# Use global wheelhouse /dir
VOLUME /wheelhouse
