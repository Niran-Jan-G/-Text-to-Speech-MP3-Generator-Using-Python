import pyttsx3
speech=pyttsx3.init()
voices=speech.getProperty('voices')
info="Success is not final, failure is not fatal: It’s the courage to keep going that counts."
speech.setProperty("voice",voices[0].id) #female voice
speech.setProperty("rate",100)
speech.setProperty("volume",1)
speech.save_to_file(info,"python.mp3")
speech.runAndWait()
print('success')