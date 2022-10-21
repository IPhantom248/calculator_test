FROM python:3.8

ARG APP_NAME=calculator_test
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /usr/src/$APP_NAME

RUN apt-get -y update && \
    apt-get -y install libc-dev build-essential python3 python3-pip

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/$APP_NAME/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/$APP_NAME/

RUN mkdir -p /usr/src/$APP_NAME

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
