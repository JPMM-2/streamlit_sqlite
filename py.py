import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st


db_file='northwind.db'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

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
