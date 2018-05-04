FROM python:3.6-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

RUN chmod 774 /usr/src/app/entrypoint.sh

# run server
CMD ["./entrypoint.sh"]