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
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit whould you like information about?', 'Kiwi')
streamlit.write('The user entered ',fruit_choice)

import snowflake.connector

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.header('Fruityvice Fruit Advice2!')
fruit_choice=streamlit.text_input('What fruit whould you like to add?', 'jackfruit')
streamlit.write('Thanks for adding ',fruit_choice)

#my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur=my_cnx.cursor()
#my_cur.execute("select current_user(), current_account(), current_region()")
#my_data_row=my_cur.fetchone()
#streamlit.text("Hello from Snwoflake:")
#streamlit.text(my_data_row)

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row=my_cur.fetchone()
streamlit.text("The current fruit load list contains")
streamlit.text(my_data_row)   

streamlit.header('Fruityvice Fruit Advice2!')
fruit_choice=streamlit.text_input('What fruit whould you like to add?', 'jackfruit')
streamlit.write('Thanks for adding ',fruit_choice)


