"""End-to-end TTS intelligibility test for ovos-tts-plugin-beepspeak.

Synthesises a small set of phrases with the real plugin, transcribes the
rendered audio back with a reference STT and scores the round-trip with
WER/CER via ovoscope. Report-only by default (TTS_MAX_WER=1.0).
"""
import os

from ovoscope.tts_intelligibility import score_tts_intelligibility

from ovos_tts_plugin_beepspeak import BeepSpeak

LANG = "en-US"
PHRASES = [
    "hello world",
    "what time is it",
    "good morning",
    "thank you",
    "see you later",
]


def test_tts_intelligibility():
    tts = BeepSpeak({"lang": LANG})
    report = score_tts_intelligibility(tts, PHRASES, lang=LANG, mode="playback")
    print(f"::TTS-INTELLIGIBILITY:: {report.to_dict()}")
    assert report.mean_wer <= float(os.environ.get("TTS_MAX_WER", "1.0"))
