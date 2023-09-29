FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN apk add git ffmpeg

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./creative-tonie.py" ]