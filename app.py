# -*- coding: utf-8 -*-
"""
Movie Recommender System Streamlit App
"""

import streamlit as st
import pickle
import pandas as pd

# Load the movie list and similarity matrix
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# Define the recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit app
def main():
    st.title('Movie Recommender System')

    # User input for movie selection
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movies['title'].values
    )

    # Button to show recommendations
    if st.button('Show Recommendations'):
        recommendations = recommend(selected_movie)
        st.write("Recommended Movies:")
        for rec in recommendations:
            st.write(rec)

if __name__ == '__main__':
    main()