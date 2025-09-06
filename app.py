import os
import openai
import streamlit as st
from datetime import datetime

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page config
st.set_page_config(page_title="MyChatBot Ultra 🤖", page_icon="🤖", layout="centered")

# Title
st.markdown("<h1 style='text-align:center;color:#4CAF50;'>MyChatBot Ultra 🤖</h1>", unsafe_allow_html=True)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# User input text box
user_input = st.text_input("You:", key="input")

# When user clicks Send and input is not empty
if st.button("Send") and user_input.strip():
    # Append user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip(),
        "time": datetime.now().strftime("%H:%M:%S")
    })

    # Prepare messages for OpenAI API (exclude any "Typing..." placeholders)
    chat_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

    try:
        # Call OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_messages,
            temperature=0.7,
            max_tokens=150,
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    # Append bot reply
    st.session_state.messages.append({
        "role": "bot",
        "content": bot_reply,
        "time": datetime.now().strftime("%H:%M:%S")
    })

# Display chat messages
for msg in st.session_state.messages:
    timestamp = f"<span style='font-size:10px;color:#888;'>{msg['time']}</span>"
    if msg["role"] == "user":
        st.markdown(
            f"<div style='background-color:#DCF8C6;padding:10px;border-radius:10px;margin:5px 0;'>"
            f"<b>You:</b> {msg['content']} {timestamp}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#EAEAEA;padding:10px;border-radius:10px;margin:5px 0;'>"
            f"<b>Bot:</b> {msg['content']} {timestamp}</div>",
            unsafe_allow_html=True
        )
