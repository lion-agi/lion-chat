import streamlit as st
import asyncio
from .utils import load_data_sources, save_data_sources

def render_chat_tab():
    st.title("LionAGI Chat")

    # Chat interface
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Data source selection
    data_sources = st.multiselect(
        "Select data sources for this conversation:",
        options=list(st.session_state.data_sources.keys()),
        key="chat_data_sources"
    )

    # Input area
    with st.container():
        prompt = st.text_input("Enter your message:", key="chat_input")
        if st.button("Send", key="send_button"):
            if prompt:
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                async def generate_response():
                    # TODO: Integrate with LionAGI package here
                    return f"Echo: {prompt}\nUsing data sources: {', '.join(data_sources)}"

                with st.spinner("Generating response..."):
                    response = asyncio.run(generate_response())
                
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.experimental_rerun()