import streamlit as st
import openai

# ---- Streamlit page config ----
st.set_page_config(page_title="AI Career Chatbot", page_icon="💬")

# ---- Title ----
st.title("💬 AI Career Chatbot (DeepSeek)")
st.write("Chat with an AI mentor to plan your career goals, skills, and study path.")

# ---- Get user API key ----
api_key = st.text_input("Enter your OpenAI API Key (sk-...)", type="password")

if api_key:
    openai.api_key = api_key

    # ---- User input ----
    user_input = st.text_input("Ask your career question:")

    if user_input:
        try:
            # ---- Call OpenAI API ----
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI career mentor."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=500
            )

            answer = response.choices[0].message['content']
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {e}")
