import os

import google.ai.generativelanguage as glm
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from dotenv import dotenv_values
from google.generativeai.types.generation_types import StopCandidateException

from code_functions import (add, get_datetime, multiply, open_apps,
                            open_websites, screenshot, shutdown)

genai.configure(api_key=dotenv_values(".env")["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest', tools=[get_datetime, open_apps, screenshot, open_websites, shutdown, add, multiply])

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
engine.setProperty('rate',180)

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("USER >> ", query)
            return query
        except Exception as e:
            return "Some error occurred during the input process ask the user to try again."

if __name__ == "__main__":
    chat = model.start_chat(enable_automatic_function_calling=True)
    chat.send_message("You are an AI desktop assistant. Give informative and helpful responses in a few short and simple sentences. Do not include markdown or emojis in your response.")
    while True:
        try:
            prompt = input("USER >> ")
            print()
            response = chat.send_message(prompt)
            print("AI >> ", response.text)

            engine.say(response.text)
            engine.runAndWait()

            print("----------------------------------------------------------------------------------------------")
        except StopCandidateException:
            print("Inappropriate or harmful request.")

            engine.say("Inappropriate or harmful request")
            engine.runAndWait()
        except KeyboardInterrupt:
            break
    