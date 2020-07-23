# Author: Milan Matoušek
# Jednoduchá kostra pro převzení hlasu na text a ten následně zpět
# na audio, bude sloužit jako kostra pro mého bota

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from io import BytesIO
import pygame
from time import sleep

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source2:
            # sum
            r.adjust_for_ambient_noise(source2, duration=0.2)
            # nahrani audia
            audio2 = r.listen(source2)

            # audio na text
            MyText = r.recognize_google(audio2, language='cs')
            # lower text
            Mytext = MyText.lower()

            # co jsem rekl
            print('Did you say {}'.format(MyText))

            # text na audio a do promenne
            mp3_fp = BytesIO()
            tts = gTTS(text=MyText, lang='cs', slow=False)
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            # pouzijeme pygame modul pro prehrani soundu v bit. podobe
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_fp)
            pygame.mixer.music.play()

            # uspani aby se nedošlo k loopingu
            sleep(1)

    except sr.RequestError as e:
        print('Could not request results; {}'.format(e))

    except sr.UnknownValueError:
        print('Unknown error occured')
