from openrouter import OpenRouter
import os

def chat(messages: list, tools: list = None, model: str = "nvidia/nemotron-3-super-120b-a12b:free"):
    with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
        response = client.chat.send(model=model, messages=messages, tools=tools)
        return response.choices[0].message
