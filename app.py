import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # activate api key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# movie recommendation system
st.title("Movie Recommendation System!")
user_input = st.text_input("Enter movie name: ")
submit = st.button("CLICK HERE")

# if submit:
    # st.markdown("Movie name has been entered")

# else:
    # st.warning("No movie name entered")

model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.markdown(f"Movie name entered:{user_input}")
    response  = model.generate_content(f"Generate Movie recomendations related to:{user_input}")
    st.write(f"Recommendations: \n {response.text}")

else:
    st.write("You need to enter movie name: ")