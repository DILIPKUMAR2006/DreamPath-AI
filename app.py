import streamlit as st
from openai import OpenAI

# ---- Streamlit page config ----
st.set_page_config(page_title="AI Career Chatbot", page_icon="💬")

st.title("💬 AI Career Chatbot (DeepSeek)")
st.write("Chat with an AI mentor to plan your career goals, skills, and study path.")

# ---- User API Key ----
api_key = st.text_input("Enter your OpenAI API Key (sk-...)", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # ---- User input ----
    user_input = st.text_input("Ask your career question:")

    if user_input:
        try:
            # ---- Use new Chat Completions API ----
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI career mentor."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=500
            )

            answer = response.choices[0].message.content
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {e}")
