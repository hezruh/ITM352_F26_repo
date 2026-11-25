import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = "openrouter/free"

response = client.chat.completions.create(
    model=MODEL,
    messages = [
    {"role": "system", "content": "You are a friendly assistant for Aloha Bikes, a bike rental shop in Waikiki. Answer in 2 sentences or less."},
    {"role": "user", "content": "What should I bring on a bike ride to Diamond Head?"}
]
)
print(response.choices[0].message.content)
