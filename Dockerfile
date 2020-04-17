ARG image_name
FROM python:$image_name
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y tmux

RUN mkdir /piteau
WORKDIR /piteau

RUN pip install piteau
