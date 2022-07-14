import streamlit as st
import pandas

st.title('Breakfast Favorites')
st.write('🥣Omega 3 & Blueberry Oatmeal')
st.write('🥬kale, Spinach & Rocket Smoothie')
st.write('🥚Hard-Boiled Free-Range Egg')
st.write('🥑🍞Avocado Toast')

st.title('🍌🍍Build Your Own Fruit Smoothie🍓🥭')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on teh page
st.dataframe(my_fruit_list)
