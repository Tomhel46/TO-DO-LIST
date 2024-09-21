import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        return ""

'''def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()'''

if __name__ == "__main__":
    while True:
        time1=[]
        user_input = input("Press 's' to start speaking or 'q' to quit: ")
        if user_input.lower() == 's':
            speech_text = recognize_speech()
            print("You said:", speech_text)
            time1.extend(speech_text)
            #text_to_speech("You said: " + speech_text)
        elif user_input.lower() == 'q':
            print("Goodbye!")






