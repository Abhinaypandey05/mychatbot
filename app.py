import os
import openai
import streamlit as st
from datetime import datetime
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="MyChatBot Ultra 🤖", page_icon="🤖", layout="centered")
st.markdown("<h1 style='text-align:center;color:#4CAF50;'>MyChatBot Ultra 🤖</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")
if st.button("Send") and user_input.strip():
    st.session_state.messages.append({"role":"user","content":user_input,"time":datetime.now().strftime("%H:%M:%S")})
    st.session_state.messages.append({"role":"bot","content":"Typing...","time":datetime.now().strftime("%H:%M:%S")})
    time.sleep(1)

    # Prepare messages for ChatCompletion
    chat_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages if m["content"] != "Typing..."]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_messages,
            temperature=0.7,
            max_tokens=150
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    st.session_state.messages[-1] = {"role":"bot","content":bot_reply,"time":datetime.now().strftime("%H:%M:%S")}

# Display chat
st.markdown("<div style='height:400px;overflow-y:auto;'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    timestamp = f"<span style='font-size:10px;color:#888;'>{msg['time']}</span>"
    if msg["role"]=="user":
        st.markdown(f"<div style='background-color:#DCF8C6;padding:10px;border-radius:10px;margin:5px 0;'><b>You:</b> {msg['content']} {timestamp}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#EAEAEA;padding:10px;border-radius:10px;margin:5px 0;'><b>Bot:</b> {msg['content']} {timestamp}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
