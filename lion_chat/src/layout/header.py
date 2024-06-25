import streamlit as st

def render_header():
    st.markdown("""
    <div class="header">
        <h1 style="margin: 0; font-size: 2.5rem;">LionAGI Showcase</h1>
        <p style="margin: 0; font-size: 1rem; color: rgb(161, 161, 170);">
            Empowering businesses with advanced AI solutions for unparalleled growth and innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)