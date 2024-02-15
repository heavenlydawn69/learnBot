import openai
import os
import json

# Create a .env file and add api key to OPENAI_API_KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = []

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def chatbot(input):
  if input:
    messages.append({"role": "user", "content": input})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message['content']  # Corrected line
    messages.append({"role": "assistant", "content": reply})
    return reply
  else:
    return "Please type something to chat with me."


while True:
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break
    response = chatbot(user_input)
    print(f"Assistant: {response}")
    knowledge_base["questions"].append({"question": user_input, "answer": response})
    save_knowledge_base('knowledge_base.json', knowledge_base)
