import streamlit as st
from chatbot import Minibot
from knowledge_base import KNOWLEDGE_BASE

# Load chatbot only once using caching
@st.cache_resource
def load_chatbot():
    return Minibot(KNOWLEDGE_BASE)

# --- Streamlit UI ---
st.title(" AlgoCorp Assistant")
st.write("Ask me anything about AlgoCorp!")

# Load the chatbot
bot = load_chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
if prompt := st.chat_input("What is your question?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from chatbot (this call now works correctly)
    response = bot.get_answer(prompt)

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
