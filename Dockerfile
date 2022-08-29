FROM python:3.9.6-alpine

ENV TZ=Europe/Moscow

WORKDIR /usr/src/simple_cms

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

RUN chmod +x /usr/src/simple_cms/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/simple_cms/entrypoint.sh"]