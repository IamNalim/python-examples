from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'cs'
zprava = 'zdravím tě'

sp = gTTS(text=zprava, lang=language, slow=False)

sp.save(audio) # ulozeni audia
playsound(audio)
