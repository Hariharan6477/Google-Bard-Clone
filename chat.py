import google.generativeai as genai


genai.configure(api_key='AIzaSyCC-yCZ7KVv7UazA_qUbmfQRjjqCsvbUWk')
model = genai.GenerativeModel('gemini-pro')

def chat(text):
    response = model.generate_content(text)
    return response.text

# from bardapi import Bard
# import os



# token ="dQjabTuUGi7ye0IoI9LbUY-peFCl0vWliPLkqoacqvqMr2eL9xwcqU6FNu34c0AvROZ3lw."

# bard = Bard(token = token)

# # while True:
# #     print()
# #     a = str(input("Ask Anything:"))
# #     print()
# #     print()
# #     if a == "thanks":
# #         break
# #     result = bard.get_answer(a)
# #     print(result['content'])


# def chat(text) :
#      return bard.get_answer(text)['content']


