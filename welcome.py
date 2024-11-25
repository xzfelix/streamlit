import streamlit as st
import time

st.title("Welcome to iamlab.cn")
st.write("智能医学实验室.")

progress_text = "Loading in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.balloons()
