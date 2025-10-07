import streamlit as st
from openai import OpenAI

# Title
st.title("💼 AI Career Assistant")
st.write("Get personalized career guidance, skill analysis, and resume suggestions!")

# Sidebar for API key
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# User input
question = st.text_area("🧠 Ask your career or skill question here:")

if st.button("Get Advice"):
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not question.strip():
        st.warning("Please type a question first.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a career mentor helping students improve skills and resumes."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.success("✨ AI Career Suggestion:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
