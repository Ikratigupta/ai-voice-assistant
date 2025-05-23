import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Command processor
def processCommand(command):
    command = command.lower()
    if 'search' in command:
        query = command.replace('search', '').strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    else:
        speak("Sorry, I didn't understand that command.")

# Main execution
if __name__ == "__main__":
    speak("Initializing, say hello to activate...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                wake_word = recognizer.recognize_google(audio)
                print(f"You said: {wake_word}")
                if wake_word.lower() == "hello":
                    speak("Yes?")
                    
                    # Listen for command
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
