import streamlit;
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.title('Idly Dosa Sambar')
streamlit.title('Chappathi Poori Tea')
streamlit.header('Build your own smoothi')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
