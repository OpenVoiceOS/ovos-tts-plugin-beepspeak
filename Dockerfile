FROM python:3.8-buster

RUN apt-get update -y && apt-get install -y libsndfile1 python3-pip sox

COPY . /tmp/ovos-tts-plugin-beepspeak

RUN pip3 install ovos-tts-server==0.0.2
RUN pip3 install /tmp/ovos-tts-plugin-beepspeak

ENTRYPOINT ovos-tts-server --engine ovos-tts-plugin-beepspeak