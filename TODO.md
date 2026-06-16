# TODO

## Open issues

- [ ] #8 Dependency Dashboard (Renovate bot meta-issue)

## Gaps

- [ ] No test suite (no `tests/` dir, no test runner configured).
- [ ] No standard gh-automations CI: missing `build-tests`, `coverage`, `license-check`, `release_workflow`, `publish_stable`, and `opm-check` (this declares a `mycroft.plugin.tts` entry point). Only a manual `publish_docker.yml` exists.
- [ ] Packaging via `setup.py` with `version='0.0.1'` hardcoded; no `pyproject.toml`. Migrate to gh-automations semver flow.
- [ ] `setup.py` `url=''` — missing Homepage pointing at `OpenVoiceOS/ovos-tts-plugin-beepspeak`.
- [ ] Committed scratch artifact: `ovos_tts_plugin_beepspeak.egg-info/` is tracked; `__pycache__/` present.
- [ ] No `master` branch — releases cannot be cut via the org's `dev`/`master` flow yet.
- [ ] README notes development was forked to `chatterbox-droid-tts`; provenance/sync status of `res/droid` assets unclear.

## Code TODOs

- `ovos_tts_plugin_beepspeak/__init__.py:79` — TODO: "do we want to spam this in every lang? add a special lang code for 'any'?" (sample config only advertises `en`).
