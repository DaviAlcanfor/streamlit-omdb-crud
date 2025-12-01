import streamlit as st
import os

from database.model.User import User
from components.page_config import pg_config
from database.dao.UserDAO import UserDAO

pg_config(page_icon="👥")
dao = UserDAO()

# ------------------------- Display Movies ------------------------
           
st.title("Users")
st.subheader("All Users in Database")

df = dao.get_all()
st.dataframe(df)


# ------------------------ Add Movie Form ------------------------
st.divider()



st.subheader("Add a New User")
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email", value="user@example.com")
    password = st.text_input("Password")
    icon = st.file_uploader("Icon")
    
    submitted = st.form_submit_button("Add User")
    
    if submitted:
        new_user = User(
            name=name,
            email=email,
            password=password,
            icon=icon
        )
        dao.create(new_user)
        st.success(f"User '{name}' added successfully!")
        st.rerun()



