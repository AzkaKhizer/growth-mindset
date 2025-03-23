import streamlit as st 
import pandas as pd 
import os 
from io import BytesIO 



st.set_page_config(page_title="Growth Mindset", layout="wide")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to your growth journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.") 

st.header("Today's Growth Mindset Quote")
st.write("The only limit to our realization of tomorrow is our doubts of today.")

st.header("What's your challenge today?")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f"You are facing {user_input}. Keep pushing forward you goal! ")     
    
else:
    st.warning("Tell us about your challenge to get started!")
    
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great insight! Your reflection : {reflection}")
    
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")
    


st.header("Celebrate you Wins!")

acheivment = st.text_input("Share something you have recently accomplished:")


if acheivment:
    st.success(f"Amazing! You have achieved: {acheivment}")
    
else:
    st.info("Big or small, every echievement counts. Share one Now!")
    
    st.write("- - -")
    st.write("Keep believing in yourself. Growth is a journey, not a destination!")    
    st.write("Created by Azka")
       
