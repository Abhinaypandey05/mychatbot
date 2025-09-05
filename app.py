


import os
import openai
import streamlit as st
from datetime import datetime
import time

# Set API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI setup
st.set_page_config(page_title="MyChatBot Ultra 🤖", page_icon="🤖", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>MyChatBot Ultra 🤖</h1>
    <p style='text-align: center; color: #555;'>Real-time AI chat with history, timestamps, and typing effect!</p>
    """,
    unsafe_allow_html=True
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []

# Input container
with st.container():
    user_input = st.text_input("You:", key="input")

    if st.button("Send"):
        if user_input.strip():
            # Append user message with timestamp
            st.session_state.messages.append({
                "role": "user",
                "content": user_input,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            try:
                # Simulate bot typing delay
                st.session_state.messages.append({
                    "role": "bot",
                    "content": "Typing...",
                    "time": datetime.now().strftime("%H:%M:%S")
                })
                time.sleep(1)  # simulate typing

                # Generate bot response using conversation history
                prompt_text = "\n".join(
                    [f"{m['role']}: {m['content']}" for m in st.session_state.messages if m['content'] != "Typing..."]
                )
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt_text,
                    max_tokens=150
                )
                bot_reply = response.choices[0].text.strip()
                # Replace typing placeholder with real reply
                st.session_state.messages[-1] = {
                    "role": "bot",
                    "content": bot_reply,
                    "time": datetime.now().strftime("%H:%M:%S")
                }

            except Exception as e:
                st.session_state.messages[-1] = {
                    "role": "bot",
                    "content": f"Error: {e}",
                    "time": datetime.now().strftime("%H:%M:%S")
                }

# Scrollable chat container
st.markdown("<div style='height:400px; overflow-y:auto;'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    timestamp = f"<span style='font-size:10px; color:#888;'>{msg['time']}</span>"
    if msg["role"] == "user":
        st.markdown(
            f"<div style='background-color:#DCF8C6; padding:10px; border-radius:10px; margin:5px 0;'>"
            f"<b>You:</b> {msg['content']} {timestamp}</div>", unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#EAEAEA; padding:10px; border-radius:10px; margin:5px 0;'>"
            f"<b>Bot:</b> {msg['content']} {timestamp}</div>", unsafe_allow_html=True
        )
st.markdown("</div>", unsafe_allow_html=True)
=======
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

