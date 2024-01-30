import streamlit;
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.title('Idly Dosa Sambar')
streamlit.title('Chappathi Poori Tea')
streamlit.header('Build your own smoothi')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

#lets put the fruits here. so that user can pickw hat they want to
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
