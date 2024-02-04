import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st

db_file='northwind.db'
conn = sqlite3.connect(db_file)
cur = conn.cursor()


name = st.sidebar.text_input('mete tu nombre')
st.session_state['password'] = st.sidebar.text_input('mete tu contrasena')

i = 5

if st.session_state['password'] not in st.session_state:
	sql_str = "select * from users where name = '" + str(name) + "' and password = " + str(st.session_state['password'])
	i = 25
	curr=cur.execute(sql_str)
	df=pd.DataFrame(curr)
	sp = df.shape[0]
else:
	i = 7


if sp == 1:
	
    sql_str = "insert into users values ('qqqq',8521)"
    cur.execute(sql_str)
    conn.commit()
        
    
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
	
elif sp == 0:
	st.sidebar.write('you do not have access to the tool')
	
st.write(i)
