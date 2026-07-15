# BeepSpeak — an R2D2-style droid "beep" voice served through ovos-tts-server's
# ElevenLabs-compatible API. A self-contained, fully offline image: the beep samples
# ship inside the package, so no network and no model download are needed at runtime.
# Any client that speaks the ovos-tts-server / ElevenLabs API can hit it, and it can be
# A/B-tested against other ovos-tts-server voices by pointing at a different port.
FROM python:3.11-slim

# sox concatenates the bundled beep samples into the final WAV; libsndfile1 backs it.
RUN apt-get update && apt-get install -y --no-install-recommends \
        sox \
        libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# the plugin (+ its bundled res/ samples) and the OVOS TTS server. setuptools<81 keeps
# ovos-plugin-manager's pkg_resources usage working. ovos-tts-server>=1.13.5a1's alpha
# floor lets pip resolve the prerelease without --pre. BeepSpeak emits WAV, so no
# transcode dependency is required.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir "setuptools<81" "." "ovos-tts-server>=1.13.5a1"

# Default droid voice, overridable with the BEEP_VOICE build arg.
ARG BEEP_VOICE=r2d2
RUN useradd -m -u 1000 ovos \
    && mkdir -p /home/ovos/.config/mycroft \
    && printf '{\n  "tts": {\n    "module": "ovos-tts-plugin-beepspeak",\n    "ovos-tts-plugin-beepspeak": {\n      "voice": "%s"\n    }\n  }\n}\n' "${BEEP_VOICE}" \
        > /home/ovos/.config/mycroft/mycroft.conf \
    && chown -R 1000:1000 /home/ovos/.config
USER 1000

EXPOSE 9666
ENTRYPOINT ["ovos-tts-server", "--engine", "ovos-tts-plugin-beepspeak", \
            "--host", "0.0.0.0", "--port", "9666", "--cache"]
