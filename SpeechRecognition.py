# speech to text Conversion using python
# with text to speech 
# "say return 0 for ending the program" 

import speech_recognition as sr 
import subprocess
import webbrowser
import os
import pyttsx3


def util(audio_text):
    if audio_Text.find("open cmd") != -1:
        subprocess.call('cmd.exe')
    elif audio_Text.find("open calculator") != -1:
        subprocess.call('calc.exe')
    elif audio_Text.find("open notepad") != -1:
        subprocess.call('notepad.exe') 
    elif audio_Text.find("open vlc") != -1:
        subprocess.call('C://Program Files (x86)//VideoLAN//VLC//vlc.exe') 
    elif audio_Text.find("open dev cpp") != -1:
        subprocess.call('C://Program Files (x86)//Dev-Cpp//devcpp.exe')
    elif audio_Text.find("open chrome") != -1:
        subprocess.call('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')
    elif audio_Text.find("open map") != -1:
        webbrowser.open('https://www.google.com/maps/')
    elif audio_Text.find("open youtube") != -1:
        webbrowser.open('https://www.youtube.com/')
    elif audio_Text.find("shutdown pc") != -1:
        os.system("shutdown /s /t 1")
    elif audio_Text.find("open whatsapp") != -1:
        webbrowser.open('https://web.whatsapp.com/') 
    else :
        print("Did u say " + audio_Text)

    speakText(audio_Text)


# Initializing the recognizer 
r = sr.Recognizer()  #r is of type speech_recognition.Recognizer 

def speakText(audio_Text):
    engine=pyttsx3.init()
    engine.say(audio_Text)
    engine.runAndWait()

# Loop infinitely for user to 
# speak 

while(True):    
    
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
        
        # using the microphone as source for input. 
        with sr.Microphone() as source: 
            
            # wait for a 0.3 second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.3) 
            
            #listening for the user's input 
            audio = r.listen(source) #is of type speech_recognition.AudioData 
            
            # Using google to recognize audio 
            audio_Text = r.recognize_google(audio) 
            audio_Text = audio_Text.lower()

            if audio_Text.find("return 0") != -1:
                break
            else:
             util(audio_Text)

            
            
     #catching exception       
    except sr.RequestError as e: 
        print("Unable to connect ,check connection ".format(e)) 
        
    except sr.UnknownValueError: 
        print(".....")