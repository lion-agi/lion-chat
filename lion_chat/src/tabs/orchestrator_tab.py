import streamlit as st
import asyncio
import lionagi as li

async def call_direct(**kwargs):
    directive_mixin = li.DirectiveMixin()
    result = await directive_mixin.direct(**kwargs)
    return result

def render_orchestrator_tab():

    # Initialize session state for chat history if it doesn't exist
    if "orchestrator_messages" not in st.session_state:
        st.session_state.orchestrator_messages = []

    # Create two columns: chat and controls
    chat_col, controls_col = st.columns(2)

    with chat_col:
        st.subheader("Chat")
        
        # Calculate the height of the chat box (matching the right side)
        chat_height = 600  # Adjust this value to match the total height of the right side controls
        
        # Create a container for the scrollable chat
        chat_container = st.container()
        
        # Display chat messages in a scrollable area
        with chat_container:
            st.markdown(f"""
                <div style="height: {chat_height}px; overflow-y: scroll; background-color: #262730; padding: 10px; border-radius: 5px;">
                    {"".join([f'<p style="margin-bottom: 10px;"><strong>{"User" if msg["is_user"] else "Assistant"}:</strong> {msg["content"]}</p>' for msg in st.session_state.orchestrator_messages])}
                </div>
            """, unsafe_allow_html=True)

        # Chat input
        user_input = st.text_input("Type your message here...")
        if st.button("Send"):
            if user_input:
                st.session_state.orchestrator_messages.append({"content": user_input, "is_user": True})
                # Here you would typically process the user input with LionAGI
                # For now, we'll just echo the message
                response = f"Received: {user_input}"
                st.session_state.orchestrator_messages.append({"content": response, "is_user": False})
                st.experimental_rerun()

    with controls_col:
        st.subheader("Orchestrator Controls")
        instruction = st.text_area("Instruction", height=100)
        context = st.text_area("Context", height=100)
        tools = st.multiselect("Tools", ["Tool1", "Tool2", "Tool3"])
        reason = st.checkbox("Reason")
        predict = st.checkbox("Predict")
        allow_action = st.checkbox("Allow Action")
        max_extension = st.number_input("Max Extension", min_value=0, max_value=10)
        imodel = st.selectbox("Model", ["GPT-3", "GPT-4", "Claude"])
        system = st.text_area("System Prompt", height=100)

        if st.button("Execute"):
            with st.spinner("Processing..."):
                result = asyncio.run(
                    call_direct(
                        instruction=instruction, 
                        context=context, 
                        tools=tools, 
                        reason=reason, 
                        predict=predict, 
                        allow_action=allow_action, 
                        max_extension=max_extension, 
                        imodel=imodel, 
                        system=system
                    )
                )
            st.session_state.orchestrator_result = result
            st.experimental_rerun()

    # Results section below chat and controls
    st.subheader("Results")
    if "orchestrator_result" in st.session_state:
        result = st.session_state.orchestrator_result
        
        # Check if the result is a dictionary
        if isinstance(result, dict):
            for key, value in result.items():
                st.markdown(f"**{key}:**")
                if isinstance(value, str):
                    st.markdown(value)
                elif isinstance(value, (list, dict)):
                    st.json(value)
                else:
                    st.write(value)
        else:
            st.markdown(result)

        # Add options to save or clear the result
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Result"):
                # Implement save functionality
                st.success("Result saved!")
        with col2:
            if st.button("Clear Result"):
                del st.session_state.orchestrator_result
                st.experimental_rerun()