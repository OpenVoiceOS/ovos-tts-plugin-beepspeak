#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-tts-plugin-beepspeak = ovos_tts_plugin_beepspeak:BeepSpeak'
setup(
    name='ovos-tts-plugin-beepspeak',
    version='0.0.1a1',
    description='droid tts plugin for OpenVoiceOS/Mycroft/Chatterbox/Neon',
    url='',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_beepspeak'],
    install_requires=["requests", 'ovos-plugin-manager>=0.0.1a4'],
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    keywords='OpenVoiceOS mycroft chatterbox ovos plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
