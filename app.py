import streamlit as st
import requests

st.set_page_config(page_title="AI Career Chatbot", page_icon="💬")

st.title("💬 AI Career Chatbot (DeepSeek)")
st.write("Chat with an AI mentor to plan your career goals, skills, and study path.")

# Get API key from secrets (safe)
api_key = st.secrets["DEEPSEEK_API_KEY"]

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if prompt := st.chat_input("Ask something about your career..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🧠 Thinking...")

        # API request to DeepSeek
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "deepseek-chat",
            "messages": st.session_state["messages"],
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                reply = result["choices"][0]["message"]["content"]
                message_placeholder.markdown(reply)
                st.session_state["messages"].append({"role": "assistant", "content": reply})
            else:
                message_placeholder.markdown("⚠️ No valid response from DeepSeek.")
        except Exception as e:
            message_placeholder.markdown(f"❌ Error: {e}")

