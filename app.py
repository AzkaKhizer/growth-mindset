import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Growth Mindset", layout="wide")

# Main Title
st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")

# Introduction Section
st.header("🌟 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.")

# Quote Section
st.header("💬 Today's Growth Mindset Quote")
st.success("*'The only limit to our realization of tomorrow is our doubts of today.' — Franklin D. Roosevelt*")

# Challenge Input Section
st.header("🚀 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:", placeholder="e.g., Learning a new skill, staying motivated")

if user_input:
    st.success(f"🌟 You are facing **{user_input}**. Keep pushing forward toward your goal!")    
else:
    st.warning("💡 Tell us about your challenge to get started!")

# Reflection Section
st.header("🔍 Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:", placeholder="What did you learn or realize from today's challenges?")

if reflection:
    st.success(f"✨ Great insight! Your reflection: *{reflection}*")
else:
    st.info("🧠 Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievement Section
st.header("🏅 Celebrate Your Wins!")
achievement = st.text_input("Share something you have recently accomplished:", placeholder="Big or small, every win counts!")

if achievement:
    st.success(f"🎉 Amazing! You have achieved: **{achievement}**")
else:
    st.info("👏 Big or small, every achievement counts. Share one now!")

# Closing Encouragement
st.markdown("---")
st.write("💪 Keep believing in yourself. Growth is a journey, not a destination!")
st.write("✨ Created by **Azka**")
