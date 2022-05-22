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

build it
```bash
docker build . -t ovos/beepspeak
```

run it
```bash
docker run -p 8080:9666 ovos/beepspeak
```

use it `http://localhost:8080/synthesize/hello`


### Notes

For a period of time development was migrated to a fork on chatterbox repositories

code was last synchronized with [chatterbox-droid-tts==0.0.1a1](https://pypi.org/project/chatterbox-droid-tts/0.0.1a1)
