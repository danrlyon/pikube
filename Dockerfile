# set base image (host OS)
FROM arm64v8/python:3

WORKDIR /usr/src/app
COPY . .
RUN pip install pyserial
CMD [ "python", "./serial-load.py" ]
