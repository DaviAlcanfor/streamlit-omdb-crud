import streamlit as st
import os

from database.model.Movie import Movie
from components.page_config import pg_config
from database.dao.MovieDAO import MovieDAO

pg_config(page_icon="🎬")
dao = MovieDAO()
AGE_GROUP = [10, 12, 14, 16, 18]


# ------------------------- Display Movies ------------------------
           
st.title("Movies")
st.subheader("All Movies in Database")

df = dao.get_all()
st.dataframe(df)


# ------------------------ Add Movie Form ------------------------
st.divider()



st.subheader("Add a New Movie")
with st.form("movie_form"):
    title = st.text_input("Title")
    year = st.number_input("Year", min_value=1800, max_value=2100, step=1)
    age_group = st.selectbox("Age Group", AGE_GROUP)
    description = st.text_area("Description")
    rating = st.number_input("Rating", min_value=0.0, max_value=10.0, step=0.1)
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=500, step=1)
    genre = st.text_input("Genre")
    
    submitted = st.form_submit_button("Add Movie")
    
    if submitted:
        new_movie = Movie(
            title=title,
            year=year,
            age_group=age_group,
            description=description,
            rating=rating,
            duration=duration,
            genre=genre
        )
        dao.create(new_movie)
        st.success(f"Movie '{title}' added successfully!")
        st.rerun()



