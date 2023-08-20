#---------------Modules---------------#
import speech_recognition as sr

#------------Variables------------#
assistant_name = "J E T T"

#---------------Functions---------------#
def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("J E T T : Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
    
    try:
        print("J E T T : Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()