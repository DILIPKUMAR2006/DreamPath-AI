import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="AI Career Chatbot", page_icon="💬")

st.title("💬 AI Career Chatbot")
st.write("Chat with an AI mentor to plan your career goals, skills, and study path.")

# Get API key from user
api_key = st.text_input("Enter your OpenAI API Key (sk-...)", type="password")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask me anything about your career:")

if st.button("Send") and user_input:
    if not api_key:
        st.error("Please enter your OpenAI API Key!")
    else:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        try:
            # Call OpenAI GPT API
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )

            # Get assistant reply
            reply = response.choices[0].message["content"]

            # Add assistant reply to session state
            st.session_state.messages.append({"role": "assistant", "content": reply})

            # Display conversation
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**AI Mentor:** {msg['content']}")

        except openai.error.AuthenticationError:
            st.error("Invalid API Key! Check your key and try again.")
        except openai.error.OpenAIError as e:
            st.error(f"OpenAI API Error: {e}")
