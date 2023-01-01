import streamlit as st
import pickle


def recommend(selected_movie_name):
    movie_index = movies_lists[movies_lists['title'] == selected_movie_name]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies_lists.iloc[i[0]].title)
    return recommended_movies

movies_list = pickle.load(open("movies.pkl","rb"))
movies_lists = movies_list['title'].values

similarity = pickle.load(open("similarity.pkl","rb"))


st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'how would you like to be contacted? ',
    (movies_lists)
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)