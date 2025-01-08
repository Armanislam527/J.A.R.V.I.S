import logging
from openai import OpenAI
from config import apikey
client = OpenAI(api_key=apikey)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a helpful assistant."},
        {"role": "user",
         "content": "Respond to this command."}
    ])
print(response.choices[0].message.content)

logging.basicConfig(level=logging.DEBUG)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a helpful assistant."},
        {"role": "user",
         "content": "What's 2+2?"}
    ])
logging.debug(response)
