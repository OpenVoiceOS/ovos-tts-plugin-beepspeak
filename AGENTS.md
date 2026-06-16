# ovos-tts-plugin-beepspeak

R2D2-style "droid beep" TTS plugin for OpenVoiceOS. Maps each character of an utterance to a pre-recorded beep WAV and concatenates them; spaces become silence clips whose duration is keyed off `time_step`.

## Setup

```bash
pip install ovos-tts-plugin-beepspeak
# from source
pip install .
```

Runtime deps: `requests`, `ovos-plugin-manager>=0.0.1`. Imports also pull in `ovos-utils`. `ConcatTTS` requires `sox` on PATH to stitch the WAV fragments (the Dockerfile installs `sox` and `libsndfile1`).

## Test

No test suite exists. There is no test command.

## Lint/Typecheck

None configured.

## Layout

- `ovos_tts_plugin_beepspeak/__init__.py` — `BeepSpeak(ConcatTTS)` engine, `BeepSpeakValidator(TTSValidator)`, and the `BeepSpeakTTSPluginConfig` sample-config dict. `sentence_to_files()` returns the list of WAV paths (no phonemes); `beep_speak()` strips characters with no matching beep and builds the file list.
- `ovos_tts_plugin_beepspeak/res/droid/` — per-character beep WAVs (`A_beep.wav`..`Z_beep.wav`, `0_beep.wav`..`9_beep.wav`, punctuation like `!_beep.wav`, `+_beep.wav`, `-_beep.wav`) and `silence01.wav`..`silence07.wav` keyed by `time_step`.
- `setup.py` — packaging; `Dockerfile` — wraps the engine in `ovos-tts-server`.
- `.github/workflows/publish_docker.yml` — manual (`workflow_dispatch`) container publish to ghcr.io.

Entry-point group: `mycroft.plugin.tts` (`ovos-tts-plugin-beepspeak = ovos_tts_plugin_beepspeak:BeepSpeak`) plus `mycroft.plugin.tts.config` for the sample config. This is an OPM TTS plugin.

## Conventions

- Branches: work on `dev`, release from `master`. NEVER use `main`. (Repo default branch is currently `dev`; there is no `master` yet.)
- Never edit a `version.py` — gh-automations bumps semver from conventional-commit prefixes (`feat:`, `fix:`, `feat!:`). This repo still pins `version='0.0.1'` inline in `setup.py`.
- New repos are private by default; do not make source public without asking.
- Commit identity: JarbasAi <jarbasai@mailfence.com>.
- Reference `OpenVoiceOS/gh-automations` reusable workflows at `@dev`. CI is provided by gh-automations.
- No Neon / `neon-*` references.
- No meta-commentary: describe current state only — no history, no dates.

## Gotchas

- `config` values `time_step`, `channels`, `rate`, `lang`, `sounds` are read at init; `time_step` is clamped to [0.1, 0.7] then string-mangled (`str(...).replace(".", "")[:2]`) to index `silenceNN.wav`. Only `silence01`..`silence07` exist, so values outside the matching range point at missing files.
- `available_languages` returns an empty `set()`; the sample config only advertises `en` even though the beep mapping is language-agnostic.
- Characters with no beep file are silently dropped from the utterance.
- The plugin relies on `ConcatTTS` from ovos-plugin-manager to actually concatenate the WAVs; behaviour depends on that base class and on `sox`.
- `setup.py` `url=''` (no Homepage); packaging predates the gh-automations standard.
