import streamlit as st
from streamlit import set_page_config
import random

ABOUT = """A simple, interactive movie CRUD app using Streamlit and the OMDb API. Search, add, and edit movies directly in your
browser while learning API integration and rapid Python web development."""
HELP = "https://github.com/DaviAlcanfor/streamlit-omdb-crud"
REPORT = "https://github.com/DaviAlcanfor/streamlit-omdb-crud/issues"

def pg_config(page_title=None, page_icon=None):
    
    set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'Get Help': HELP,
            'Report a bug': REPORT,
            'About': ABOUT
        }
    )