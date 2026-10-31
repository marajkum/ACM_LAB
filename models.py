import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.environ["OPENROUTER_API_KEY"],
)

models = [
    "openai/gpt-4o-mini",               
    "meta-llama/llama-3.3-70b-instruct",
]

prompt = "Explain what an API key is in two sentences."

for model in models:
    response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}],)
    print(f"=== {model} ===")
    print(response.choices[0].message.content)
    print()