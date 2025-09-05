
from openai import OpenAI

# Apni API key yahan daalo
client = OpenAI(api_key="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")

# Chat history store karne ke liye
history = [
    {"role": "system", "content": "You are a helpful, friendly AI assistant. Reply in Hinglish if user mixes Hindi and English."}
]

print("🤖 Smart Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("🤖 Chatbot: Bye 👋, take care!")
        break

    # User ka message history me add karo
    history.append({"role": "user", "content": user})

    try:
        # ChatGPT API se reply lao
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # fast + sasta model
            messages=history,
            temperature=0.7        # creativity control
        )

        reply = response.choices[0].message.content
        print("🤖 Chatbot:", reply)

        # Assistant ka reply bhi history me add karo
        history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Error:", e)
=======
from openai import OpenAI

# Apni API key yahan daalo
client = OpenAI(api_key="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")

# Chat history store karne ke liye
history = [
    {"role": "system", "content": "You are a helpful, friendly AI assistant. Reply in Hinglish if user mixes Hindi and English."}
]

print("🤖 Smart Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("🤖 Chatbot: Bye 👋, take care!")
        break

    # User ka message history me add karo
    history.append({"role": "user", "content": user})

    try:
        # ChatGPT API se reply lao
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # fast + sasta model
            messages=history,
            temperature=0.7        # creativity control
        )

        reply = response.choices[0].message.content
        print("🤖 Chatbot:", reply)

        # Assistant ka reply bhi history me add karo
        history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Error:", e)
