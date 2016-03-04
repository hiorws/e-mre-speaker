#!/usr/bin/python
# -*- coding: utf-8 -*-

___author___ = 'hiorws'

from gtts import gTTS

speak_list = ['Kankaa', 'Kankaa', 'Kanka devreyi ne yaptın?', 'Dota Kanka', 'Prophet', 'Panda',
 			'Kanki bunlarla da kreplere yatarsan adam degilsin kanki.',
 			'Kanki naptın?', 'Faynayt sıktı be kanki.',
 			'Aynen kanka.', 'Aynen kanki aynen.', 'aynen',
 			 'aynen', 'aynen', 'aynen', 'aynen', 'aynen kanki aynen', 'aynen',
 			 'aynen']

tts = gTTS(text=' '.join(speakList), lang='tr')

tts.save("emrebot.mp3")
