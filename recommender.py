import streamlit as st
import numpy as np
import pickle
import pandas as pd

st.title("Movie recommender system")
pt = pickle.load(open('pt.pkl', 'rb'))
similarities = pickle.load(open('sim.pkl',"rb"))
url = pickle.load(open('final.pkl',"rb"))


def recommend(book_name):
    try:
        index = np.where(pt.index==book_name)[0][0]
        lis = sorted(list((enumerate(similarities[index]))),key = lambda x:x[1],reverse=True)[1:6]
        names= []
        for i in lis:
            book_name = pt.index[i[0]]
            link = url[url['Book-Title'] == book_name]['Image-URL-L'].values[0]
            names.append((book_name,link))
        return names
    except:
        return "This book has not listed yet\nPlease try some other movie"



# print(recommend('Animal Farm'))


query = st.text_input("Search", placeholder="Type to search...")


if st.button("Recommand"):
    lis = recommend(query)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(lis[0][0])
        st.image(lis[0][1])

    with col2:
        st.text(lis[1][0])
        st.image(lis[1][1])

    with col3:
        st.text(lis[2][0])
        st.image(lis[2][1])

    with col4:
        st.text(lis[3][0])
        st.image(lis[3][1])

    with col5:
        st.text(lis[4][0])
        st.image(lis[4][1])





