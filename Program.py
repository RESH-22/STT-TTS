import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """Convert microphone speech to text."""
    with sr.Microphone() as source:
        print("Listening... Speak now.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Network error!")
        return ""

def main():
    print("---- Speech to Text & Text to Speech ----")

    while True:
        print("\n1. Speech to Text")
        print("2. Text to Speech")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = speech_to_text()
            if text:
                speak("You said " + text)

        elif choice == "2":
            text = input("Enter text to speak: ")
            speak(text)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

# Run the project
main()
