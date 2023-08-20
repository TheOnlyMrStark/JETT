#---------------Modules---------------#
import pyttsx3

#------------Variables------------#
assistant_name = "J E T T"

#---------------Functions---------------#
def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 180)
    print("        ")
    print(f"J E T T : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("        ")
    