import streamlit as st
from .utils import get_data_sources, remove_data_source

def render_manage_sources():
    st.subheader("Manage Data Sources")

    sources = get_data_sources()
    for idx, source in enumerate(sources):
        with st.expander(f"{source['name']} ({source['type']})"):
            st.write(f"Type: {source['type']}")
            if source['type'] == 'api':
                st.write(f"URL: {source['url']}")
                st.write(f"API Type: {source['api_type']}")
            elif source['type'] == 'database':
                st.write(f"Database Type: {source['db_type']}")
                st.write(f"Username: {source['username']}")
            elif source['type'] == 'file':
                st.write(f"File Name: {source['details']['FileName']}")
                st.write(f"File Size: {source['details']['FileSize']} bytes")
            
            if st.button(f"Remove {source['name']}", key=f"remove_{idx}"):
                remove_data_source(idx)
                st.success(f"Removed data source: {source['name']}")
                st.rerun()

    if st.button("Clear All Data Sources"):
        st.session_state.data_sources = []
        st.success("All data sources have been cleared.")
        st.rerun()