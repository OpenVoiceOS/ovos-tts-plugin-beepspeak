# beep speak TTS

## Description

OpenVoiceOS R2D2 TTS plugin 

## Install

```bash
pip install ovos-tts-plugin-beepspeak
```

## Configuration


```json
  "tts": {
    "module": "ovos-tts-plugin-beepspeak",
    "ovos-tts-plugin-beepspeak": {
      "time_step": 0.1
    }
 }
```


## Docker

Serve the voice behind [ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server)
(ElevenLabs-compatible API) on port 9666. The image is fully self-contained and
offline — the beep samples ship inside the package, so no network or model download is
needed at runtime.

Pull the prebuilt image:

```bash
docker run -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-beepspeak:dev
```

…or build locally:

```bash
docker build -t ovos-tts-plugin-beepspeak .
docker run -p 9666:9666 ovos-tts-plugin-beepspeak
```

…or with compose:

```bash
docker compose up
```

Synthesize: `http://localhost:9666/synthesize/hello`

The served voice defaults to `r2d2` and can be changed at build time:

```bash
docker build --build-arg BEEP_VOICE=r2d2 -t ovos-tts-plugin-beepspeak .
```


### Notes

For a period of time development was migrated to a fork on chatterbox repositories

code was last synchronized with [chatterbox-droid-tts==0.0.1a1](https://pypi.org/project/chatterbox-droid-tts/0.0.1a1)
