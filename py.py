import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st

db_file='northwind2.db'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

st.write('Below is a DataFrame:')

name = st.sidebar.text_input('mete tu nombre')
password = st.sidebar.text_input('mete tu contrasena')



if st.button('login'):


	sql_str = "select * from users where name = '" + str(name) + "' and password = " + str(password)

	print(sql_str)

	curr=cur.execute(sql_str)
	df=pd.DataFrame(curr)


	if df.shape[0] == 1:

		sql_str = "SELECT name FROM sqlite_master where type = 'table'"
		curr=cur.execute(sql_str)
		df=pd.DataFrame(curr)
		lst = df[0].tolist()

		tbl = st.sidebar.selectbox('Select the table', lst)
		sql_str     = 'select * from ' + str(tbl) 

		curr=cur.execute(sql_str)
		df=pd.DataFrame(curr)

		#print (lst)

		st.dataframe(df)
		
	elif df.shape[0] == 0:
		st.sidebar.write('you do not have access to the tool')
