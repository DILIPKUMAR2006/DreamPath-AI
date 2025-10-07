import streamlit as st
import requests

# Streamlit app title
st.title("💼 AI Career Assistant (DeepSeek Powered)")
st.write("Ask career questions, get AI advice, and resume improvement tips!")

# Sidebar for API key
api_key = st.sidebar.text_input("Enter your DeepSeek API Key", type="password")

# User question input
question = st.text_area("🧠 Ask your career or skill question:")

if st.button("Get Career Advice"):
    if not api_key:
        st.error("Please enter your DeepSeek API key in the sidebar.")
    elif not question.strip():
        st.warning("Please enter a question first.")
    else:
        try:
            # DeepSeek API endpoint
            url = "https://api.deepseek.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are an AI career mentor helping students with skill guidance and resumes."},
                    {"role": "user", "content": question}
                ]
            }

            response = requests.post(url, headers=headers, json=data)
            result = response.json()

            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
                st.success("✨ AI Career Suggestion:")
                st.write(answer)
            else:
                st.error("No valid response from DeepSeek. Check your API key or quota.")

        except Exception as e:
            st.error(f"Error: {e}")
