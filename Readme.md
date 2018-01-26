# beep speak TTS

this is a TTS engine for mycroft, using r2d2 sounds, why should an AI have a
human voice?

Each beep corresponds to a letter, so you can learn to understand beep speak!

# install

edit the files at the following directories

    github install: /path/mycroft-core/mycroft/tts
    mark 1: /usr/local/lib/python2.7/site-packages/mycroft_core-0.9.14-py2.7.egg/mycroft/tts

add beep_speak_tts.py to this directory

edit _init_.py, it should be safe to simply replace the file with the one provided

    class TTSFactory(object):
        ....
        from mycroft.tts.ibm_tts import WatsonTTS
        from mycroft.tts.beep_speak_tts import BeepSpeak

        CLASSES = {
            ....
            "bing": BingTTS,
            "beepspeak": BeepSpeak
        }


copy the sound files to the following directory

    github install: /path/mycroft-core/mycroft/res/beep_speak
    mark 1: /usr/local/lib/python2.7/site-packages/mycroft_core-0.9.14-py2.7.egg/mycroft/res/snd/beep_speak


# usage

change your config file, if it does not exist, create it

    ~/.mycroft/mycroft.conf

the config must be valid json

    {

        "tts": {
        "module": "beepspeak",
        "beepspeak": {
                "time_step": 0.3
            }
        }

    }

that's it! mycroft should now speak like r2d2, you edit the time_step
parameter to tune the beeping speed