import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.utilities import SearxSearchWrapper

def show_page():
    llm = Ollama(model="llama3.1:8b-instruct-q8_0", base_url="https://e9e8-35-240-168-164.ngrok-free.app")
    s = SearxSearchWrapper(searx_host="http://localhost:8888")



    st.title("Talk to Stock Guru")

    if "chats" not in st.session_state:
        st.session_state.chats = []

    if st.session_state.chats:
        for message in st.session_state.chats:
            if message["type"] == "user":
                st.chat_message("user").write(message["content"])
            else:
                st.chat_message("assistant").write(message["content"])

    if user_input := st.chat_input("Ask about stocks, e.g., AAPL vs MSFT vs GOOGL"):
        st.session_state.chats.append({"type": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        try:
            context = s.run(user_input, engines=["google"])
            prompt = f"Context: {context}\nQuestion: {user_input}\nPrompt: Always provide with an answer"
            response = llm.invoke(prompt)
        
        except Exception as e:
            response = f"Error: {e}"

        st.session_state.chats.append({"type": "assistant", "content": response})
        st.chat_message("assistant").write(response)