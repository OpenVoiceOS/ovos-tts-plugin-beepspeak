from os.path import join, dirname

from ovos_plugin_manager.templates.tts import ConcatTTS, TTSValidator
from ovos_utils.log import LOG


class BeepSpeak(ConcatTTS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs,
                         validator=BeepSpeakValidator(self))
        self.time_step = float(self.config.get("time_step", 0.1))
        if self.time_step < 0.1:
            self.time_step = 0.1
        if self.time_step > 0.7:
            self.time_step = 0.7
        self.time_step = str(self.time_step).replace(".", "")[:2]
        self.voice = self.config.get("voice", "r2d2")
        self.channels = self.config.get("channels", "1")
        self.rate = self.config.get("rate", "16000")
        self.lang = self.config.get("lang", "en-us")
        self.sound_files_path = self.config.get("sounds",
                                                join(dirname(__file__), "res", "droid"))

    def sentence_to_files(self, sentence):
        phonemes = None
        return self.beep_speak(sentence), phonemes

    def beep_speak(self, sentence):
        valid = ["?", "!", ".", "+", "-", "*", "A", "B", "C", "D", "E",
                 "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                 "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1",
                 "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for char in sentence:
            if char.upper() not in valid and char != ' ':
                LOG.warning('Error the character ' + char + ' cannot be ' \
                                                            'translated to ' \
                                                            'beep_speak')
                sentence = sentence.replace(char.upper(), "").replace(char, "")
        files = []
        for char in sentence:
            if char == ' ':
                files.append(
                    self.sound_files_path + "/silence" + self.time_step + '.'
                    + self.audio_ext)
            else:
                files.append(
                    self.sound_files_path + "/" + char.upper() + '_beep.' +
                    self.audio_ext)
        return files


class BeepSpeakValidator(TTSValidator):
    def __init__(self, tts):
        super(BeepSpeakValidator, self).__init__(tts)

    def get_tts_class(self):
        return BeepSpeak
