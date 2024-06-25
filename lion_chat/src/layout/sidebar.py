import streamlit as st
from data_sources.utils import get_data_sources

def render_sidebar():
    st.sidebar.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #1e293b;
        }
        .sidebar-content h1, .sidebar-content h2, .sidebar-content h3 {
            color: #eab308;
        }
        .sidebar-content .stSelectbox > div > div > select {
            background-color: #334155;
            color: #e2e8f0;
        }
        .sidebar-content .stSlider > div > div > div > div {
            background-color: #eab308;
        }
        .sidebar-content .stButton > button {
            background-color: #334155;
            color: #e2e8f0;
        }
        .sidebar-content .stButton > button:hover {
            background-color: #475569;
        }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("LionAGI Dashboard")

    st.sidebar.header("LLM Configuration")
    model = st.sidebar.selectbox("Select LLM Model", ["GPT-3", "GPT-4", "Claude"])
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.sidebar.number_input("Max Tokens", 1, 2048, 256)

    st.sidebar.header("LionAGI Info")
    st.sidebar.info(f"LionAGI Version: {st.session_state.get('app_version', '1.0.0')}")
    
    lionagi_status = "Connected"
    st.sidebar.success(f"Status: {lionagi_status}")

    st.sidebar.header("Data Sources")
    data_source_counts = count_data_sources()
    for source_type, count in data_source_counts.items():
        st.sidebar.metric(f"{source_type} Sources", count)

    st.sidebar.header("Current Configuration")
    st.sidebar.json({
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "Total Data Sources": sum(data_source_counts.values()),
    })

    st.sidebar.header("Quick Actions")
    if st.sidebar.button("Clear All Data"):
        clear_all_data()
        st.sidebar.success("All data cleared!")

    if st.sidebar.button("Export Configuration"):
        export_configuration()
        st.sidebar.success("Configuration exported!")

def count_data_sources():
    data_sources = get_data_sources()
    counts = {}
    for source in data_sources:
        source_type = source['type']
        counts[source_type] = counts.get(source_type, 0) + 1
    return counts

def clear_all_data():
    st.session_state.data_sources = []
    st.session_state.agents = []
    st.session_state.tasks = []

def export_configuration():
    st.sidebar.text("Configuration exported (placeholder)")