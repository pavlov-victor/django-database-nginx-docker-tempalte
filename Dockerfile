FROM python:3.8
ENV PYTHONUNBUFFERED 1
ADD config/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN apt-get update
RUN apt-get -y install gcc libffi-dev libssl-dev libxml2-dev libxslt-dev swig && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 adduser --disabled-password --gecos '' user

USER user