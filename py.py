import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st


list_tbl = ['Territories','Suppliers','Employees','EmployeeTerritories']

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            

db_file='northwind.db'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

tbl = st.sidebar.selectbox('Select the table', list_tbl)

sql_str     = 'select * from ' + str(tbl) 

#where symbol= + symbol

curr=cur.execute(sql_str)


df=pd.DataFrame(curr)



print (df)


st.dataframe(df)