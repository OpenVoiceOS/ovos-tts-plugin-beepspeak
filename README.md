# ovos-tts-plugin-beepspeak

A text-to-speech plugin for [OVOS](https://github.com/OpenVoiceOS) that speaks in R2D2-style
beeps instead of words. It maps each letter, digit, and a few punctuation marks to a beep
sound file, then concatenates the files into one audio stream. It works fully offline
because the beep samples ship inside the package.

## Install

```bash
pip install ovos-tts-plugin-beepspeak
```

## Configuration

Add this to your OVOS TTS configuration:

```json
  "tts": {
    "module": "ovos-tts-plugin-beepspeak",
    "ovos-tts-plugin-beepspeak": {
      "time_step": 0.1
    }
 }
```

`time_step` sets the length of the silence between beeps, in seconds. Valid values range
from 0.1 to 0.7. The plugin clamps out-of-range values to the nearest limit.

## Docker

Serve the voice behind [ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server)
(an ElevenLabs-compatible API) on port 9666. The image is self-contained and offline. The
beep samples ship inside the package, so the server needs no network access or model
download at runtime.

Pull the prebuilt image:

```bash
docker run -p 9666:9666 ghcr.io/openvoiceos/ovos-tts-plugin-beepspeak:dev
```

Or build it locally:

```bash
docker build -t ovos-tts-plugin-beepspeak .
docker run -p 9666:9666 ovos-tts-plugin-beepspeak
```

Or run it with compose:

```bash
docker compose up
```

Synthesize a phrase: `http://localhost:9666/synthesize/hello`

The served voice defaults to `r2d2`. Change it at build time:

```bash
docker build --build-arg BEEP_VOICE=r2d2 -t ovos-tts-plugin-beepspeak .
```

### History

For a period, development moved to a fork under the chatterbox repositories. The code here
was last synchronized with [chatterbox-droid-tts==0.0.1a1](https://pypi.org/project/chatterbox-droid-tts/0.0.1a1).

## Related projects

- [OpenVoiceOS](https://github.com/OpenVoiceOS) — the voice assistant platform this plugin
  extends.
- [ovos-tts-server](https://github.com/OpenVoiceOS/ovos-tts-server) — serves this plugin
  over an ElevenLabs-compatible HTTP API.
- [ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager) — the plugin
  interface this TTS engine implements.
