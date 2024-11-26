
from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command ='''' '''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Aditya who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Aditya"},
    {"role": "user", "content": command }
  ]
)

print(completion.choices[0].message.content)