
# docker image build for a node in the simulation
FROM ubuntu:latest

# update the image to the latest packages
RUN apt-get update && apt-get upgrade -y
# add ip features
RUN apt install -y iproute2 
# enable ping between devices
RUN apt-get install -y iputils-ping

# python dev utils
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

# set the cwd and files
WORKDIR /home
COPY . .

RUN pip install -r requirements.txt

