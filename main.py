import vertexai
from vertexai.preview.generative_models import (FunctionDeclaration,
                                                GenerativeModel, Part, Tool)

from code_functions import *

PROJECT_ID = "bamboo-velocity-429404-u2"
tools = Tool(function_declarations=[
    FunctionDeclaration(
        name="get_datetime",
        description="""Gets current system date and time.
        Parameters:
            None
        Returns:
            string: current datetime
        """,
        parameters={
            "type": "object",
            "properties": {
            }
        }
    ),
    FunctionDeclaration(
        name="open_apps",
        description="""Opens the given apps.
        Parameters:
            string: app name
        Returns:
            None
        """,
        parameters={
            "type": "object",
            "properties": {
                "app_name": {
                    "type": "string",
                    "description": "Name of the app to be opened"
                }
            }
        }
    ),
])

vertexai.init(project=PROJECT_ID)

model = GenerativeModel("gemini-pro", generation_config={"temperature": 0},tools=[tools])
chat = model.start_chat()

function_handlers = {
    "get_datetime": get_datetime,
    "open_apps": open_apps,
}

if __name__ == "__main__":
    while True:
        try: 
            prompt = input("PROMPT >> ")
            print()
            response = chat.send_message(prompt)
    
            function_call = response.candidates[0].content.parts[0].function_call
            if function_call.name in function_handlers:
                function_name = function_call.name               

                args = {key: value for key, value in function_call.args.items()}

                function_response = function_handlers[function_name](**args)

                response = chat.send_message(
                    Part.from_function_response(
                        name=function_name,
                        response={
                            "content": function_response
                        }
                    ),
                )

            print("RESPONSE >> ", response.candidates[0].content.parts[0].text)
            print("-------------------------------------------------------------")
        except KeyboardInterrupt:
            break
