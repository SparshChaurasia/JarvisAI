import os
import tkinter as tk
from tkinter import ttk

import google.ai.generativelanguage as glm
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from dotenv import dotenv_values
from google.generativeai.types.generation_types import StopCandidateException
from PIL import Image, ImageTk

from code_functions import (add, get_datetime, multiply, open_apps,
                            open_websites, screenshot, shutdown)

genai.configure(api_key=dotenv_values(".env")["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest', tools=[get_datetime, open_apps, screenshot, open_websites, shutdown, add, multiply])

# Text to Speech engine congfiguration
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
engine.setProperty('rate',180)


def voice_input() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            
            return query
        except Exception as e:
            return "Some error occurred during the input process ask the user to try again."
    

def ai_response(prompt: str) -> None:  
    try:
        print("USER >> ", prompt)

        response = chat.send_message(prompt)

        print("AI >> ", response.text)

        engine.say(response.text)
        engine.runAndWait()

        print("----------------------------------------------------------------------------------------------")
    except StopCandidateException:
        print("Inappropriate or harmful request.")

        engine.say("Inappropriate or harmful request")
        engine.runAndWait()


def text_input_wrapper(event=None):
    # print(event)
    ai_response(inputtxt.get(1.0, "end-1c") )
    inputtxt.delete(1.0, tk.END)


def voice_input_wrapper():
        def close_panel():
            label.destroy()
            close_btn.destroy()
    
        label = tk.Label(
            root,
            text="Listening...",
            width=20,
            height=12,
            font=("Source Code Pro", 15, "bold"),
        )
        close_btn = tk.Button(root, command=close_panel, text="x", width=2, height=1)

        label.place(x=0, y=0)
        close_btn.place(x=0, y=0)

        query = voice_input()
        label.destroy()

        ai_response(query)
        

if __name__ == "__main__":
    chat = model.start_chat(enable_automatic_function_calling=True)
    chat.send_message("You are an desktop AI assistant. Give short and helpful responses. Do not include markdown or emojis in your response.")

    root = tk.Tk()
    
    w = 250 
    h = 270
    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight() 
    x = ws - w
    y = hs - (h+30)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Desktop Assistant")
    # root.configure(background="blue")
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.resizable(False, False)
    # root.overrideredirect(True)
    # root.bind_class("all", "<Ctrl+E>", root.iconify)
    
    base_width = 65
    img = Image.open("./media/chatbot-icon-removebg.png")
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)

    tk.Label(root, image=img).pack()
    tk.Label(root, text="DESKTOP ASSISTANT", font=("Source Code Pro", 12, "bold")).pack()


    frame = tk.Frame(root)
    frame.pack()

    inputtxt = tk.Text(
                    frame,
                    height=2,
                    width=23, 
                    font=("Source Code Pro", 12),
                    bg="white"
                ) 
    inputtxt.grid(row=0, column=0, columnspan=2, pady=15) 

    run = tk.Button(frame, text="RUN ⌨", font=("Source Code Pro", 12, "bold"), command=text_input_wrapper)
    run.grid(row=1, column=0, sticky="news")
    root.bind("<Return>", text_input_wrapper)
    tk.Button(frame, text="VOICE 🔊", font=("Source Code Pro", 12, "bold"), command=voice_input_wrapper).grid(row=1, column=1, sticky="news")
    # tk.Button(frame, text="EXIT ❌", font=("Source Code Pro", 12, "bold"), command=root.destroy).grid(row=2, column=0, columnspan=2, sticky="news")

    root.mainloop()
    