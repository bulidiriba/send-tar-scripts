FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install python3-pip python3-dev -y

# set the working directory
WORKDIR /app
# copy the requirements.txt 
COPY ./requirements.txt /app/requirements.txt
# install the required package
RUN pip3 install -r requirements.txt
# copy all the files in current directory to working directory
COPY . /app
# the command to start the flask app
CMD python3 app.py