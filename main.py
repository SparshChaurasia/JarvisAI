from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv(".env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a story about a AI and magic")
print(response.text)
