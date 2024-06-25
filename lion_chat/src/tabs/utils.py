import json
import os
import streamlit as st

def save_data_sources():
    with open("data_sources.json", "w") as f:
        json.dump(st.session_state.data_sources, f)

def load_data_sources():
    if os.path.exists("data_sources.json"):
        with open("data_sources.json", "r") as f:
            return json.load(f)
    return {}