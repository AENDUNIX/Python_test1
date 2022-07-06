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









# ###########
# # BUILDER #
# ###########
# # pull official base image
# FROM python:3.8.3-alpine as builder
# # set work directory
# WORKDIR /usr/src/app
# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# # install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev && apk add -u zlib-dev
# # lint
# RUN pip install --upgrade pip
# RUN pip install --upgrade Pillow
# COPY . .
# # install dependencies
# COPY ./requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# #########
# # FINAL #
# #########
# # pull official base image
# FROM python:3.8.3-alpine
# # create directory for the app user
# RUN mkdir -p /home/app
# # create the app user
# RUN addgroup -S app && adduser -S app -G app
# # create the appropriate directories
# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# WORKDIR $APP_HOME
# # install dependencies
# # RUN apk update && apk add libpq
# # COPY --from=builder /usr/src/app/wheels /wheels
# # COPY --from=builder /usr/src/app/requirements.txt .
# # RUN pip install --no-cache /wheels/*
# # copy entrypoint-prod.sh
# #COPY ./entrypoint.sh $APP_HOME
# # copy project
# COPY . $APP_HOME
# # chown all the files to the app user
#
# # run entrypoint.prod.sh
# #ENTRYPOINT ["/home/app/web/entrypoint.sh"]