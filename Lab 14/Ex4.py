import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from mycontent import build_system_prompt, MENU, INFO

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = "openrouter/free"

system_context = input("Enter system context (or press Enter to use default): ")

if not system_context.strip():
    system_context = "You are a helpful assistant for aloha bikes."

messages = [{"role": "system", "content": system_context}]
print("welcome to your custom chatbot. type 'exit' or 'quit' to end the chat.")


while True:
    user_text = input("You: ")
    if user_text.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    if not user_text.strip():
        print("Please enter a valid message.")
        continue
    messages.append({"role": "user", "content": user_text})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"Assistant: {reply}")

    messages.append({"role": "assistant", "content": reply})