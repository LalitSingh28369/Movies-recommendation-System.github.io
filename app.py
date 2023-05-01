import streamlit as st
import pandas as pd
import pickle


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies_list=pickle.load(open('movies.pkl','rb')) #hmovies_list holds the new_df dataframe.  rb-->read binary
movies=pd.DataFrame(movies_list)
movies_list=movies_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'How would you  like to be contacted?',
movies_list)

if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)