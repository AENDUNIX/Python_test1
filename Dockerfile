FROM python:3.9.6-alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./pip-requirements.txt .
RUN pip install --no-cache-dir -r req.txt

COPY . .
COPY ./startpoint.sh /usr/src/app/startpoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/startpoint.sh
RUN chmod +x /usr/src/app/startpoint.sh
ENTRYPOINT ["/usr/src/app/startpoint.sh"]

RUN mkdir -p /home/app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
