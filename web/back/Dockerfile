FROM python:3.8.13

ENV PYTHONUNBUFFERED=0
ENV PATH=~/.local/bin:$PATH
ENV TZ=Asia/Seoul

WORKDIR /app
ADD ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update &&\
    apt-get install libgl1-mesa-glx -y &&\
    apt-get install libglib2.0-0 -y &&\
    apt-get install ffmpeg x264 libx264-dev -y &&\
    apt-get install watch -y
