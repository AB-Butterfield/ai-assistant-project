from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 for male, 1 for female
activationWord = 'computer' #Kiko?
# sr.adjust_for_ambient_noise(source, duration=5)

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source) 
    print('Listening for your command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I didnt quite catch that')
        speak('Sah ry I didnt catch that')
        print(exception)
        return 'None'
    
    return query

# Main loop

if __name__ == '__main__':
    speak('Booted up and ready to help, captain')

    while True:
        # Parse as a list
        query = parseCommand().lower().split()
        print(query)
        if query[0] == activationWord:
            query.pop(0)
            print(query)
            # List commands
            
            if query[0] == 'say':
                if query[1] == 'your':
                    if query[2] == 'name':
                        print("Hello. My name is Kiko.")
                        speak("Hello. My name is Kiko.")
                if 'hello' in query:
                    speak('Hello!')
                else:
                    query.pop(0) #remove say
                    speech = ' '.join(query)
                    speak(speech)



