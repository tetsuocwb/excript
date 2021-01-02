import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
names = voices[0].name
for idx,voz in enumerate(voices):
    print(idx,voz.name,voz.gender,voz.languages, voz.age)
print(names)
engine.setProperty('voice', voices[22].id)
engine.setProperty('rate', 160)
print(engine.setProperty.__code__.co_varnames)
# engine.say("MARMITá ?")
# engine.say("MARMITá ?")
engine.say("e aii  aíury, ta com saudade?")
print(rate)
engine.runAndWait()