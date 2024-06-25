import streamlit as st
from streamlit_elements import elements, mui, html
from agent.agents_tab import render_agents_tab
from tabs.orchestrator_tab import render_orchestrator_tab
from data_sources.data_sources_tab import render_data_sources_tab
from layout.header import render_header
from layout.footer import render_footer
from data_sources.utils import load_data_sources, get_data_sources
from data_sources.api_sources import render_api_sources
import uuid

def set_global_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        :root {
            --background: 24, 24, 24;
            --foreground: 240, 240, 240;
            --muted: 144, 144, 144;
            --accent: 210, 140, 50;
            --accent-dark: 170, 110, 40;
            --card: 34, 34, 34;
            --sidebar: 28, 28, 28;
            --input-bg: 44, 44, 44;
            --gradient-start: 28, 28, 28;
            --gradient-end: 24, 24, 24;
            --contrast: 50, 50, 50;
        }
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }
        
        .stApp {
            background: linear-gradient(180deg, rgba(var(--gradient-start), 1), rgba(var(--gradient-end), 1));
            color: rgb(var(--foreground));
        }
        
        .sidebar .sidebar-content {
            background-color: rgba(var(--sidebar), 0.95);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-right: 1px solid rgba(var(--muted), 0.2);
        }
        
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            background-color: rgb(var(--input-bg));
            color: rgb(var(--foreground));
            border: 1px solid rgba(var(--muted), 0.2);
            border-radius: 8px;
        }
        
        .stSlider > div > div > div > div {
            background-color: rgb(var(--accent));
        }
        
        .stButton > button {
            background-color: rgb(var(--accent));
            color: rgb(var(--background));
            font-weight: 500;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: rgb(var(--accent-dark));
        }
        
        .stTab > button {
            color: rgba(var(--foreground), 0.7);
        }
        
        .stTab > button[data-baseweb="tab"][aria-selected="true"] {
            color: rgb(var(--accent));
            border-bottom: 2px solid rgb(var(--accent));
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: rgb(var(--accent));
            font-weight: 500;
        }
        
        /* Custom classes */
        .card {
            background-color: rgb(var(--card));
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .text-muted {
            color: rgb(var(--muted));
        }

        .header {
            position: sticky;
            top: 0;
            z-index: 999;
            background-color: rgb(var(--background));
            padding: 1rem;
            margin-left: -4rem;
            margin-right: -4rem;
            margin-top: -4rem;
            padding-left: 4rem;
            padding-right: 4rem;
            padding-top: 3rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background-color: rgb(var(--background));
            padding: 1rem;
            box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.2);
        }

        .main-content {
            margin-bottom: 60px;
            padding: 1rem;
            background-color: rgb(var(--contrast));
        }

        /* Hide Streamlit's default header */
        header {
            display: none !important;
        }

        /* Adjust sidebar to not overlap with header */
        .sidebar-content {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.title("LionAGI Dashboard")

    st.sidebar.header("LLM Configuration")
    model = st.sidebar.selectbox("Select LLM Model", ["GPT-3", "GPT-4", "Claude"])
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.sidebar.number_input("Max Tokens", 1, 2048, 256)

    st.sidebar.header("API Data Sources")
    render_api_sources()

    st.sidebar.header("Data Source Summary")
    data_sources = get_data_sources()
    data_source_counts = {}
    for source in data_sources:
        source_type = source['type']
        data_source_counts[source_type] = data_source_counts.get(source_type, 0) + 1
    
    for source_type, count in data_source_counts.items():
        st.sidebar.metric(f"{source_type.capitalize()} Sources", count)

def main():
    # Set page config
    st.set_page_config(page_title="LionAGI Showcase", layout="wide", page_icon="🦁")

    # Set global styles
    set_global_styles()

    # Set app version
    st.session_state['app_version'] = "1.0.0"

    # Initialize session state
    if "data_sources" not in st.session_state:
        st.session_state.data_sources = load_data_sources()
    if "agents" not in st.session_state:
        st.session_state.agents = []

    # Render header
    render_header()

    # Render sidebar
    render_sidebar()

    # Main content
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Main content area
    tab1, tab2, tab3 = st.tabs(["Agents", "LionAGI Orchestrator", "Data Sources"])

    with tab1:
        render_agents_tab()

    with tab2:
        render_orchestrator_tab()

    with tab3:
        render_data_sources_tab()

    st.markdown('</div>', unsafe_allow_html=True)

    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
