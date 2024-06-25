import streamlit as st
from .api_sources import render_api_sources
from .database_sources import render_database_sources
from .local_files import render_local_files
from .manage_sources import render_manage_sources

def render_data_sources_tab():
    
    data_source_tabs = st.tabs(["API", "Database", "Local Files", "Manage Sources"])
    
    with data_source_tabs[0]:
        render_api_sources()
    
    with data_source_tabs[1]:
        render_database_sources()
    
    with data_source_tabs[2]:
        render_local_files()
    
    with data_source_tabs[3]:
        render_manage_sources()