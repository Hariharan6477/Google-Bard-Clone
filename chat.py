from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token ="dQjabTuUGi7ye0IoI9LbUY-peFCl0vWliPLkqoacqvqMr2eL9xwcqU6FNu34c0AvROZ3lw."

bard = Bard(token = token)

# # while True:
# #     print()
# #     a = str(input("Ask Anything:"))
# #     print()
# #     print()
# #     if a == "thanks":
# #         break
# #     result = bard.get_answer(a)
# #     print(result['content'])


def chat(text) :
     return bard.get_answer(text)['content']