ARG image_name
FROM python:$image_name

RUN mkdir /piteau
WORKDIR /piteau

RUN pip install poetry
