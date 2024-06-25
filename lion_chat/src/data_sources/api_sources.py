import streamlit as st
from data_sources.utils import add_data_source, get_data_sources
import uuid

def render_api_sources():
    with st.sidebar.expander("Add New API Source"):
        with st.form(key=f"add_api_source_{uuid.uuid4()}"):
            name = st.text_input("API Name")
            url = st.text_input("API URL")
            api_key = st.text_input("API Key", type="password")
            api_type = st.selectbox("API Type", ["REST", "GraphQL", "SOAP"])

            if st.form_submit_button("Add API Source"):
                if name and url:
                    new_source = {
                        "type": "api",
                        "name": name,
                        "url": url,
                        "api_key": api_key,
                        "api_type": api_type
                    }
                    add_data_source(new_source)
                    st.success(f"Added API source: {name}")
                else:
                    st.error("Please provide both API Name and URL.")

    st.sidebar.subheader("Existing API Sources")
    api_sources = [source for source in get_data_sources() if source["type"] == "api"]
    for index, source in enumerate(api_sources):
        with st.sidebar.expander(f"{source['name']} ({source['api_type']})"):
            st.write(f"URL: {source['url']}")
            st.write(f"API Type: {source['api_type']}")
            if st.button(f"Remove {source['name']}", key=f"remove_api_{index}"):
                st.session_state.data_sources.remove(source)
                st.success(f"Removed API source: {source['name']}")
                st.rerun()