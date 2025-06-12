FROM python:3.8

MAINTAINER Omar Moreno <omoreno@slac.stanford.edu>

# Update the image and install dependencies.
RUN apt-get update &&  \
    apt-get install -y \ 
        git

# Install all external packages into /opt.
WORKDIR /opt

RUN git clone https://github.com/omar-moreno/scdms_monitor.git

# Start the crawler when the container is run. The directory /local is expected
# to point to the current working directory from which the container is run.
WORKDIR scdms_monitor
CMD ["python3", "monitory.py"]
