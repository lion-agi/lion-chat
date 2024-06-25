import streamlit as st
from streamlit_elements import elements, mui, html
from .agent_utils import create_agent, get_all_agents

def render_agents_tab():
    with elements("agents_tab"):
        mui.Typography("Agent Management", variant="h4", sx={"mb": 3, "color": "rgb(210, 140, 50)"})

        with mui.Grid(container=True, spacing=3):
            with mui.Grid(item=True, xs=12, md=6):
                with mui.Paper(sx={"p": 3, "bgcolor": "rgb(34, 34, 34)", "borderRadius": "12px"}):
                    mui.Typography("Create Agent", variant="h6", sx={"mb": 2, "color": "rgb(210, 140, 50)"})
                    
                    agent_name = st.text_input("Agent Name", key="agent_name")
                    agent_description = st.text_area("Description", key="agent_description", height=100)
                    
                    capabilities_options = [
                        "Natural Language Processing",
                        "Computer Vision",
                        "Reinforcement Learning"
                    ]
                    agent_capabilities = st.multiselect(
                        "Capabilities",
                        options=capabilities_options,
                        key="agent_capabilities"
                    )
                    
                    if st.button("Create Agent", key="create_agent_button"):
                        create_agent(agent_name, agent_description, agent_capabilities)

            with mui.Grid(item=True, xs=12, md=6):
                with mui.Paper(sx={"p": 3, "bgcolor": "rgb(34, 34, 34)", "borderRadius": "12px"}):
                    mui.Typography("Existing Agents", variant="h6", sx={"mb": 2, "color": "rgb(210, 140, 50)"})
                    agents = get_all_agents()
                    for agent in agents:
                        with mui.Card(sx={"mb": 2, "bgcolor": "rgb(36, 41, 47)", "borderRadius": "12px"}):
                            mui.CardContent(
                                children=[
                                    mui.Typography(agent.name, variant="h6", sx={"color": "rgb(240, 240, 240)"}),
                                    mui.Typography(agent.description, variant="body2", sx={"mb": 1, "color": "rgb(144, 144, 144)"}),
                                    mui.Chip(label=", ".join(agent.capabilities), size="small", sx={"bgcolor": "rgb(210, 140, 50)", "color": "rgb(24, 24, 24)"})
                                ]
                            )

    # You can still use Streamlit components for parts that are not easily replicated with MUI
    st.markdown("### Agent Statistics", unsafe_allow_html=True)
    st.metric("Total Agents", len(agents))

