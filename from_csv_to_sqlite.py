import sqlite3
import pandas as pd


conn = sqlite3.connect('api_yamdb/db.sqlite3')

data = pd.read_csv('api_yamdb/static/data/comments.csv')

data.to_sql(name='reviews_comment', con=conn, index=False, if_exists='append')

conn.close()
