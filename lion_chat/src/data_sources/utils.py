import streamlit as st

def get_data_sources():
    if 'data_sources' not in st.session_state:
        st.session_state.data_sources = []
    return st.session_state.data_sources

def add_data_source(source):
    st.session_state.data_sources.append(source)

def remove_data_source(index):
    st.session_state.data_sources.pop(index)

def load_data_sources():
    # This function can be expanded to load data sources from a file or database
    return get_data_sources()