# app.py - Safe Version

import os
import openai

# API key environment variable se le rahe hain
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simple example: text completion
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Testing
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Bot response:", generate_response(user_input))
