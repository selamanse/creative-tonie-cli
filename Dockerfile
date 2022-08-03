FROM python:3.9-alpine

WORKDIR /usr/src/app

RUN apk add git ffmpeg

RUN git clone https://github.com/moritzj29/tonie_api.git /usr/src/tonie_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./creative-tonie.py" ]