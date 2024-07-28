# Script to host ChatGPT functions - taken from other Inversity projects of Chris'

from openai import OpenAI
from dotenv import load_dotenv

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def comprehend_data(input_data):

    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                 {"role": "system", 
                  "content": """This is an MVP for loading large numbers of research papers into an AI to digest them.
                  For the purposes of this exercise, we need ChatGPT to read the data given (which is a research paper
                  transposed into text within Python) and then to succinctly relay back the objective of the paper, and the
                  THREE most important findings. The content that the user inputs will be the research paper, so please use
                  that instead of prompting for more info.
                  """},
                {"role": "user",
                 "content": input_data }
            ]
        )

    output = completion.choices[0].message.content

    print(output)

    return output