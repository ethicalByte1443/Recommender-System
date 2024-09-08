import streamlit as st
import pickle
import pandas as pd
import requests
# def get_poster(movie_id):
#     response=requests.get(
#         'https://api.themoviedb.org/3/movie/{ }?api_key=<<Your api key>>&language=en-US'.format(movie_id))
#     data =     response.json()
#     return data['poster_path']
#
#     response = requests.get(url, headers=headers)
#
#     print(response.text)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies_list = []
    for i in movie_list:
        movie_id = i[0]

        recommend_movies_list.append(movies.iloc[i[0]].title)
    return recommend_movies_list


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")


selected_movie_name = st.selectbox(
    "Search here...",
    movies['title'].values,
)

st.write("You selected:", selected_movie_name)


if st.button("Recommend"):
    st.write(recommend(selected_movie_name))
    st.write(selected_movie_name)
else:
    st.write("Goodbye")