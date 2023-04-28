#!/usr/bin/env python
# coding: utf-8

# In[17]:

import base64
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pickle


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)





# Loading data
df=pd.read_csv("all_movies.csv")
cosine_sim=pickle.load(open("C:/Users/Gamze/Movie Recommendation System/similar_movies.pickle",'rb'))

# Function to make movie recommendations
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




# Main function to run the app
def main():

    st.title("Movie Recommendation App")
    movie_name = st.text_input("Movie Name:")
    set_background("C:/Users/Gamze/Downloads/movie.jpg")
    if st.button('Get Movies'):
        recommendations = prediction_movie(movie_name)
        st.write("Recommended movies:")
        for movie in recommendations:
            st.write("- " + movie)

if __name__ == '__main__':
    main()
    


# In[ ]:





