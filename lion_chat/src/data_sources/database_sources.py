import streamlit as st
from .utils import add_data_source, get_data_sources

def render_database_sources():
    st.subheader("Database Data Sources")

    with st.form("add_database_source"):
        name = st.text_input("Database Name")
        db_type = st.selectbox("Database Type", ["MySQL", "PostgreSQL", "MongoDB", "SQLite"])
        connection_string = st.text_input("Connection String")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Add Database Source"):
            if name and connection_string:
                new_source = {
                    "type": "database",
                    "name": name,
                    "db_type": db_type,
                    "connection_string": connection_string,
                    "username": username,
                    "password": password
                }
                add_data_source(new_source)
                st.success(f"Added database source: {name}")
            else:
                st.error("Please provide both Database Name and Connection String.")

    st.subheader("Existing Database Sources")
    db_sources = [source for source in get_data_sources() if source["type"] == "database"]
    for source in db_sources:
        with st.expander(f"{source['name']} ({source['db_type']})"):
            st.write(f"Database Type: {source['db_type']}")
            st.write(f"Username: {source['username']}")