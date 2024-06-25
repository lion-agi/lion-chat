import streamlit as st
from .utils import add_data_source, get_data_sources

def render_local_files():
    st.subheader("Local File Data Sources")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "json", "txt"])
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        
        name = st.text_input("Enter a name for this data source:")
        if st.button("Add File Source"):
            if name:
                new_source = {
                    "type": "file",
                    "name": name,
                    "details": file_details,
                    "content": uploaded_file.getvalue().decode("utf-8")
                }
                add_data_source(new_source)
                st.success(f"Added file source: {name}")
            else:
                st.error("Please enter a name for the data source.")

    st.subheader("Existing File Sources")
    file_sources = [source for source in get_data_sources() if source["type"] == "file"]
    for source in file_sources:
        with st.expander(f"{source['name']} ({source['details']['FileType']})"):
            st.write(f"File Name: {source['details']['FileName']}")
            st.write(f"File Size: {source['details']['FileSize']} bytes")