from gtts import gTTS
from playsound import playsound
import io
import random

t=random.randint(0,100)
t=str(t)
text="ടോക്കൺ നമ്പർ"+t
t1="token number"+t
t2="टोकन नंबर"+t

f=io.open("token.txt",mode="w")
f.write(text)

a = gTTS(text,lang='ml')

a.save("t.mp3")
playsound("t.mp3")
f.close()
f=io.open("token.txt",mode="w")
f.write(t1)

a = gTTS(t1,lang='en')

a.save("t.mp3")
playsound("t.mp3")
f.close()
f=io.open("token.txt",mode="w")
f.write(t2)

a = gTTS(t2,lang='hi')

a.save("t.mp3")
playsound("t.mp3")