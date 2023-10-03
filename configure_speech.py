# import pyttsx3
# import webbrowser

# DON'T DO IT THIS WAY

# # Speech engine initialisation
# def start_speech_engine():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id) # 0 for male, 1 for female
#     activationWord = 'computer' #Kiko?
#     # sr.adjust_for_ambient_noise(source, duration=5)

#     # Configure browser
#     chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    
#     def speak(text, rate = 150):
#         engine.setProperty('rate', rate)
#         engine.say(text)
#         engine.runAndWait()