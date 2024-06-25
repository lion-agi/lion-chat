import streamlit as st
from .agent_models import Agent, Task

def get_all_agents():
    if 'agents' not in st.session_state:
        st.session_state.agents = []
    return st.session_state.agents

def create_agent(agent: Agent):
    if 'agents' not in st.session_state:
        st.session_state.agents = []
    st.session_state.agents.append(agent)

def update_agent(updated_agent: Agent):
    for i, agent in enumerate(st.session_state.agents):
        if agent.id == updated_agent.id:
            st.session_state.agents[i] = updated_agent
            break

def delete_agent(agent_id: str):
    st.session_state.agents = [agent for agent in st.session_state.agents if agent.id != agent_id]

def get_all_tasks():
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    return st.session_state.tasks

def assign_task(task: Task):
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    st.session_state.tasks.append(task)

def update_task_status(task_id: str, new_status: str):
    for task in st.session_state.tasks:
        if task.id == task_id:
            task.status = new_status
            break