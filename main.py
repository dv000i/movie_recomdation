import streamlit as st
import pickle
import pandas as pd
import requests
import json
def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=84370af70321fc5d77ebef2e4ce3655d&language=en-US".format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/'+ data['poster_path']


st.set_page_config(layout="wide")


def rec(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommend_movie = []
    recommend_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie_poster.append(fetch_poster(movie_id))
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie,recommend_movie_poster


similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movies_dict.pickle', 'rb'))
movies = pd.DataFrame(movies_dict)
# print(eval(movies))

st.title("Movies Recommender system")

selected_movie_name = st.selectbox("how",movies['title'].values)

if st.button('Recommend'):
    name,poster= rec(selected_movie_name)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col1:
        st.text(name[2])
        st.image(poster[2])
    with col2:
        st.text(name[4])
        st.image(poster[4])
    with col3:
        st.text(name[5])
        st.image(poster[5])
    with col1:
        st.text(name[6])
        st.image(poster[6])
    with col2:
        st.text(name[7])
        st.image(poster[7])
    with col3:
        st.text(name[8])
        st.image(poster[8])

