import streamlit as st
import pandas as pd
import pickle
import requests #library required to hit api

def fetch_poster(movie_id):
    response=requests.get(https://api.themoviedb.org/3/movie/{}?api_key=c9c5e79090bc113999348b808f3ca870&language=en-US.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommendesd_movies_posters=[]
    for i in movies_list:
        movie_id =i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommened_movies_poster



movies_list=pickle.load(open('movies.pkl','rb')) #hmovies_list holds the new_df dataframe.  rb-->read binary
movies=pd.DataFrame(movies_list)
movies_list=movies_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'How would you  like to be contacted?',
movies_list)

if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)