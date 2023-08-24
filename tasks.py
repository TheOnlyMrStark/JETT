#--------------Modules-------------#
import datetime
from speak import Say
import os
import pyautogui as pg

#------------Non-input Functions--------------#
def time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)
    
def date():
    date = datetime.date.today()
    Say(date)
    
def nonInputExecution(query):
    
    query = str(query)
    
    if "time" in query:
        time()
    elif "date" in query:
        date()
        
#-------------Input Functions-----------------#
def inputExecution(tag, query):
    
    if "wikipedia" in tag:
        name = str(query).replace("", "")#.replace("who is","").replace("what is","").replace("tell me about","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name, sentences = 2)
        Say(result)
        
    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit as pop
        pop.search(query)
        
    elif "downloads" in tag:
        Say("Ok Sir")
        os.startfile("C:\\Users\\jetma\\Downloads")
        
    elif "switch" in tag:
        pg.hotkey('alt', 'tab')