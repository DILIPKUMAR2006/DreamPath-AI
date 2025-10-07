import streamlit as st
import requests
import json

# Streamlit page configuration
st.set_page_config(page_title="AI Career Chatbot", page_icon="💬")

st.title("💬 AI Career Chatbot (DeepSeek)")
st.write("Chat with an AI mentor to plan your career goals, skills, and study path.")

# Input field for API key
api_key = st.text_input("Enter your DeepSeek API Key (sk-...)", type="password").strip()

if api_key:
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Ask your career question:")

    if user_input:
        # Append user message to chat history
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Prepare API request payload
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful AI career mentor."},
                {"role": "user", "content": user_input}
            ],
            "stream": False
        }

        # Set headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Send POST request to DeepSeek API
        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            # Extract assistant's reply from API response
            reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response from assistant.")
            # Append assistant's reply to chat history
            st.session_state["messages"].append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
else:
    st.warning("Please enter your DeepSeek API key to start chatting.")
