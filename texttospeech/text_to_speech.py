from gtts import gTTS
import os

mytext = 'merhababenibrahimyılmazinstagramdaondörtmilyontakipçimvar'
language = 'tr'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("speech.mp3")
os.system("start speech.mp3")