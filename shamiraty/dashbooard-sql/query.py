import sqlite3
import pandas as pd


# fetch
def view_all_data():
    # conncetion
    conn = sqlite3.connect('mydb.db')
    # create curso 
    c = conn.cursor()
    c.execute('SELECT * FROM insurance order by id asc')
    data = c.fetchall()
    # commit or command
    conn.commit()
    # close or connection
    conn.close()
    return data 

if __name__ == '__main__':
    dados = view_all_data()
    print(dados)
    