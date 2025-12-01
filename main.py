import streamlit as st
import os

from components.page_config import pg_config
from database.dao.MainDAO import MainDAO

pg_config(page_icon="🏠")
dao = MainDAO()

st.title("Welcome to MovieDB!")


movies_count = dao.get_movies_count()
users_count = dao.get_users_count()
    
st.subheader(f"- Total Movies: {movies_count}")
st.subheader(f"- Total Users: {users_count}")
