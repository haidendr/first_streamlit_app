import streamlit as st
import pandas

st.title('Breakfast Favorites')
st.write('🥣Omega 3 & Blueberry Oatmeal')
st.write('🥬kale, Spinach & Rocket Smoothie')
st.write('🥚Hard-Boiled Free-Range Egg')
st.write('🥑🍞Avocado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
