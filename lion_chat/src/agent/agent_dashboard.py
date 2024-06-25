import streamlit as st
import pandas as pd
import plotly.express as px
from .agent_utils import get_all_agents, get_all_tasks

def render_agent_dashboard():
    st.subheader("Agent Dashboard")

    agents = get_all_agents()
    tasks = get_all_tasks()

    if not agents:
        st.warning("No agents have been created yet. Please create some agents first.")
        return

    if not tasks:
        st.warning("No tasks have been assigned yet. Please assign some tasks first.")
        return

    # Agent Performance Chart
    agent_performance = pd.DataFrame([
        {
            "Agent": agent.name,
            "Tasks Completed": len([task for task in tasks if task.agent_id == agent.id and task.status == "Completed"]),
            "Tasks In Progress": len([task for task in tasks if task.agent_id == agent.id and task.status == "In Progress"]),
            "Tasks Not Started": len([task for task in tasks if task.agent_id == agent.id and task.status == "Not Started"])
        } for agent in agents
    ])

    if not agent_performance.empty:
        fig = px.bar(agent_performance, x="Agent", y=["Tasks Completed", "Tasks In Progress", "Tasks Not Started"], title="Agent Task Performance")
        st.plotly_chart(fig)
    else:
        st.info("No performance data available yet.")

    # Task Status Overview
    task_status = pd.DataFrame([
        {"Status": status, "Count": len([task for task in tasks if task.status == status])}
        for status in ["Not Started", "In Progress", "Completed"]
    ])

    if not task_status.empty:
        fig = px.pie(task_status, values="Count", names="Status", title="Task Status Overview")
        st.plotly_chart(fig)
    else:
        st.info("No task status data available yet.")

    # Agent Capability Distribution
    all_capabilities = set([cap for agent in agents for cap in agent.capabilities])
    capability_dist = pd.DataFrame([
        {"Capability": cap, "Count": sum(1 for agent in agents if cap in agent.capabilities)}
        for cap in all_capabilities
    ])

    if not capability_dist.empty:
        fig = px.bar(capability_dist, x="Capability", y="Count", title="Agent Capability Distribution")
        st.plotly_chart(fig)
    else:
        st.info("No agent capability data available yet.")