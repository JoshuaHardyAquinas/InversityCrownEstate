# Test script to test ChatGPT - taken from other Inversity projects of Chris'

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

question = input("What would you like to ask ChatGPT? ")

completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                 {"role": "system", 
                  "content": """This is a test run of the ChatGPT API for a project.
                  """},
                {"role": "user",
                 "content": question }
            ]
        )

answer = completion.choices[0].message.content

print(answer)