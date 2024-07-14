import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

PROJECT_ID = "bamboo-velocity-429404-u2"

vertexai.init(project=PROJECT_ID)

model = GenerativeModel("gemini-pro")
chat = model.start_chat()

if __name__ == "__main__":
    while True:
        try: 
            prompt = input("PROMPT >> ")
            print()
            response = chat.send_message(prompt)
            print("RESPONSE >> ", response.candidates[0].content.parts[0].text)
            print("-------------------------------------------------------------")
        except KeyboardInterrupt:
            break
