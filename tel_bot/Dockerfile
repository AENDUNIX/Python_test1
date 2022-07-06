FROM python:3.9.6-alpine
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install aiogram
RUN pip install requests

# Сopy project
COPY . .

CMD [ "python", "./telegram.py" ]


