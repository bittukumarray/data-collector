FROM python:3.6-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD . /code/
RUN pip3 install -r requirement.txt
RUN cd ./data_collection
COPY . /code/