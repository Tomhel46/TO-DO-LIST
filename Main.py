import datetime as dt
import time as t
import speech_recognition as sr
import pyttsx3
work_= ""
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
        user_input = input("Press 's' to start speaking or 'q' to quit: ")
       for i in range(2):
        if user_input.lower() == 's':
            speech_text = recognize_speech()
            print("You said:", speech_text)
            work_= speech_text
            #text_to_speech("You said: " + speech_text)
            print("Enter deadline date and time in yyyy/mm/dd/hour/min/sec")
            time1 = []
            for i in range(6): 
              temp = int(input("Enter one term at a time: "))
              time1.append(temp)
            target_time = dt.datetime(*time1)
            time_difference = target_time - dt.datetime.now()
            delay_seconds = time_difference.total_seconds()
            t.sleep(delay_seconds)
            print("You need to complete work:", work_)
            from twilio.rest import Client
            SID='# SID given by the twillio website '
            token='#Token given for the mobile number'
            ct=Client(SID,token)
            ct.messages.create(body=work_,from_='# number given by the twillio',to='# Enter the mobile number of the user')
        elif user_input.lower() == 'q':
            print("Goodbye!")
       