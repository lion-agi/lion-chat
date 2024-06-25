import streamlit as st
from .agent_models import Task
from .agent_utils import get_all_tasks, update_task_status, assign_task, get_all_agents
import uuid

def render_task_tracking():
    st.subheader("Task Tracking")

    tasks = get_all_tasks()

    for task in tasks:
        with st.expander(f"Task: {task.description}"):
            st.text_area("Task ID", value=task.id, disabled=True)
            st.text_area("Agent ID", value=task.agent_id, disabled=True)
            st.text_area("Status", value=task.status, disabled=True)

            new_status = st.selectbox(f"Update Status for Task {task.id}", ["Not Started", "In Progress", "Completed"], index=["Not Started", "In Progress", "Completed"].index(task.status))
            
            if new_status != task.status:
                if st.button(f"Update Status for Task {task.id}"):
                    update_task_status(task.id, new_status)
                    st.success(f"Task {task.id} status updated to {new_status}")
                    st.rerun()

    st.subheader("Assign New Task")
    with st.form("assign_task"):
        description = st.text_input("Task Description")
        agents = get_all_agents()
        agent_options = {f"{agent.name} ({agent.id})": agent.id for agent in agents}
        selected_agent = st.selectbox("Assign to Agent", options=list(agent_options.keys()))
        
        if st.form_submit_button("Assign Task"):
            if description and selected_agent:
                agent_id = agent_options[selected_agent]
                new_task = Task(id=str(uuid.uuid4()), agent_id=agent_id, description=description, status="Not Started")
                assign_task(new_task)
                st.success(f"Task assigned to agent {selected_agent}")
            else:
                st.error("Please provide a task description and select an agent.")