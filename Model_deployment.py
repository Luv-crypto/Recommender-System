import streamlit as st
import pickle
import pandas as pd
import requests
 
# Getting the Posters through API

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7e876377c3bb61cd6c2a44aacb5409a6&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function for displaying recommendations

def recommendation(MOVIE):
    movie_index = movies[movies["title"] == MOVIE].index[0]
    distance = similarity[movie_index]
    final_movies = sorted(list(enumerate(distance)), reverse = True , key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = [] 
    for i in final_movies:
                                                        # fetch the movie poster
        movieid = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(get_poster(movieid))
    return recommended_movies,recommended_movies_posters

# loading through Pickle
movies_dict= pickle.load(open("movies.pkl","rb"))
movies = pd.DataFrame(movies_dict)

similarity  =  pickle.load(open("Similarity.pkl","rb"))

# Window title
st.title("Movie Recommender System")

#Dropdown for list of movies
MOVIES = st.selectbox("Select a movie",movies["title"].values)

if st.button("Recommend"):
    recommended_movies,recommended_movies_posters = recommendation(MOVIES)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])

