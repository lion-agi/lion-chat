import streamlit as st
from .agent_models import Agent
from .agent_utils import create_agent
import uuid

def render_agent_creation():
    st.subheader("Agent Creation")

    with st.form("create_agent"):
        name = st.text_input("Agent Name")
        description = st.text_area("Description")
        capabilities = st.multiselect("Capabilities", ["Natural Language Processing", "Image Recognition", "Data Analysis"])

        if st.form_submit_button("Create Agent"):
            if name and description:
                new_agent = Agent(id=str(uuid.uuid4()), name=name, description=description, capabilities=capabilities)
                create_agent(new_agent)
                st.success(f"Agent {name} created successfully!")
            else:
                st.error("Please provide a name and description for the agent.")