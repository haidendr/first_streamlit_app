import streamlit as st
import pandas

st.title('Breakfast Favorites')
st.write('🥣Omega 3 & Blueberry Oatmeal')
st.write('🥬kale, Spinach & Rocket Smoothie')
st.write('🥚Hard-Boiled Free-Range Egg')
st.write('🥑🍞Avocado Toast')

st.title('🍌🍍Build Your Own Fruit Smoothie🍓🥭')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
st.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
