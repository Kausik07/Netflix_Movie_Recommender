import streamlit as st
from src.hybrid import hybrid_recommend

st.title("🎬 Hybrid Movie Recommender")
user_id = st.number_input("Enter User ID:", min_value=1, value=1)
movie_title = st.selectbox("Choose a Movie:", pd.read_csv("../data/processed/movie_data.csv")["title"])

if st.button("Recommend"):
    recommendations = hybrid_recommend(user_id, movie_title)
    st.write("Top Recommendations:")
    st.dataframe(recommendations)