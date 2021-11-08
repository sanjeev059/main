# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirement.txt /usr/src/app
RUN pip install -r requirement.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000
RUN cd /usr/src/app/login_module

CMD ["python", "login_module/manage.py", "runserver", "0.0.0.0:8000"]
