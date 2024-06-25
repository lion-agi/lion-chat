import streamlit as st
from .agent_models import Agent
from .agent_utils import get_all_agents, update_agent, delete_agent

def render_agent_management():
    st.subheader("Agent Management")

    agents = get_all_agents()

    for agent in agents:
        with st.expander(f"Agent: {agent.name}"):
            st.text_area("Agent ID", value=agent.id, disabled=True)
            st.text_area("Description", value=agent.description, disabled=True)
            st.text_area("Capabilities", value=", ".join(agent.capabilities), disabled=True)

            if st.button(f"Edit {agent.name}"):
                edit_agent(agent)

            if st.button(f"Delete {agent.name}"):
                delete_agent(agent.id)
                st.rerun()

def edit_agent(agent):
    with st.form(f"edit_agent_{agent.id}"):
        name = st.text_input("Name", agent.name)
        description = st.text_area("Description", agent.description)
        capabilities = st.multiselect("Capabilities", ["Natural Language Processing", "Image Recognition", "Data Analysis"], default=agent.capabilities)

        if st.form_submit_button("Update Agent"):
            updated_agent = Agent(id=agent.id, name=name, description=description, capabilities=capabilities)
            update_agent(updated_agent)
            st.success(f"Agent {name} updated successfully!")
            st.rerun()