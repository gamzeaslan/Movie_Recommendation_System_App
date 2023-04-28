#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pickle
df=pd.read_csv("all_movies.csv")

cosine_sim=pickle.load(open("C:/Users/Gamze/Movie Recommendation System/similar_movies.pickle",'rb'))

def prediction_movie(movie_name):
    df["Title"]=df["Title"].str.lower()
    movie_name=movie_name.lower()
    try:
        movie_name = df[df['Title'] == movie_name].index.values[0]
    except IndexError:
        return ["Movie not found. Please enter a valid movie name."]
        
    similar_movies = list(enumerate(cosine_sim[movie_name]))
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[0:]
    rec_movie=[]
    for i in range(10):
        rec_movie.append(((df.iloc[sorted_similar_movies[i][0]]['Title']).title()))
    return rec_movie

def main ():
    st.title("Movie Recommendation App")
    movie_name=st.text_input("Movie Name: ")
    
    diagnosis=""
    if st.button("Get Movies"):
        diagnosis = prediction_movie(movie_name)
        st.write("Recommended movies:")
        for movie in diagnosis:
            st.write("- " + movie)
        


if __name__ == '__main__':
    main()


# In[ ]:




