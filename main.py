import os

import google.ai.generativelanguage as glm
import google.generativeai as genai
from google.generativeai.types.generation_types import StopCandidateException
from dotenv import dotenv_values

from code_functions import get_datetime, open_apps, screenshot, open_websites, shutdown

genai.configure(api_key=dotenv_values(".env")["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest', tools=[get_datetime, open_apps, screenshot, open_websites, shutdown])


if __name__ == "__main__":
    chat = model.start_chat(enable_automatic_function_calling=True)
    chat.send_message("You are an AI desktop assistant. Give informative and helpful responses in a few short and simple sentences without markdown.")
    while True:
        try:
          prompt = input("USER >> ")
          print()
          response = chat.send_message(prompt)
          print("AI >> ", response.text)
          print("----------------------------------------------------------------------------------------------")
        except StopCandidateException:
            print("Inappropriate or harmful request.")
        except KeyboardInterrupt:
            break
    