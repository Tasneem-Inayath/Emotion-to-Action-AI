import streamlit as st
import requests

st.title("💬 Emotion → Action Chatbot")

# session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.messages = []

# display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# step-based conversation
def bot_message(text):
    st.session_state.messages.append({"role": "assistant", "content": text})
    with st.chat_message("assistant"):
        st.write(text)

def user_message(text):
    st.session_state.messages.append({"role": "user", "content": text})
    with st.chat_message("user"):
        st.write(text)

# STEP FLOW
if st.session_state.step == 0:
    bot_message("How are you feeling today?")
    st.session_state.step = 1

user_input = st.chat_input("Type here...")

if user_input:

    user_message(user_input)

    # Step 1 → text
    if st.session_state.step == 1:
        st.session_state.data["text"] = user_input
        bot_message("How many hours did you sleep?")
        st.session_state.step = 2

    # Step 2 → sleep
    elif st.session_state.step == 2:
        st.session_state.data["sleep"] =  int(user_input.strip())
        bot_message("What is your stress level (0–10)?")
        st.session_state.step = 3

    # Step 3 → stress
    elif st.session_state.step == 3:
        st.session_state.data["stress"] = int(user_input)
        bot_message("What is your energy level (0–10)?")
        st.session_state.step = 4

    # Step 4 → energy
    elif st.session_state.step == 4:
        st.session_state.data["energy"] = int(user_input)
        bot_message("What time of day is it? (morning/afternoon/evening/night)")
        st.session_state.step = 5

    # Step 5 → time + API call
    elif st.session_state.step == 5:
        st.session_state.data["time"] = user_input

        # call API
        url = "http://127.0.0.1:8000/predict"
        response = requests.post(url, json=st.session_state.data)

        if response.status_code == 200:
            data = response.json()

            reply = f"""
            **State:** {data['state']}  
            **Intensity:** {data['intensity']}  

            **Action:** {data['action']} ({data['when']})  

            💡 {data['message']}  

            🔍 Confidence: {round(data['confidence'], 2)}  
            ⚠️ Uncertain: {"Yes" if data['uncertain_flag'] == 1 else "No"}
            """
        else:
            reply = "⚠️ API error"

        bot_message(reply)

        # reset for next conversation
        st.session_state.step = 0
        st.session_state.data = {}