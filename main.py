import os

import google.ai.generativelanguage as glm
import google.generativeai as genai
from dotenv import dotenv_values

from code_functions import get_datetime, open_apps, screenshot

genai.configure(api_key=dotenv_values(".env")["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest', tools=[get_datetime, open_apps, screenshot])


if __name__ == "__main__":
    chat = model.start_chat(enable_automatic_function_calling=True)
    while True:
      try:
        prompt = input("USER >> ")
        print()
        response = chat.send_message(prompt)
        print("AI >> ", response.text)
        print("----------------------------------------------------------------------------------------------")
      except KeyboardInterrupt:
        break