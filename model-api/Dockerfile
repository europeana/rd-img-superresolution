FROM ubuntu:20.04

WORKDIR /code
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y git

RUN apt-get install -y python3.9 \
    && ln -s /usr/bin/python3.9 /usr/bin/python3

RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-pip

RUN pip install fire
RUN pip install Flask

RUN git clone https://github.com/joseed-europeana/image-super-resolution.git
RUN python3 image-super-resolution/setup.py install

COPY . /code
CMD python3 api.py


