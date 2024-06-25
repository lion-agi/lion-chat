import streamlit as st
import datetime

def render_footer():
    current_year = datetime.datetime.now().year
    version = st.session_state.get('app_version', '1.0.0')
    
    st.markdown(f"""
    <div class="footer">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span>© {current_year} LionAGI. All rights reserved.</span>
            <div>
                <span style="margin-right: 1rem;">v{version}</span>
                <a href="https://github.com/your-repo" target="_blank" style="color: #D4AF37; margin-right: 1rem;">GitHub</a>
                <a href="https://docs.lionagi.ai" target="_blank" style="color: #D4AF37;">Documentation</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)