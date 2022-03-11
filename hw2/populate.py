import pandas as pd
import numpy as np
import sqlite3 
from sqlite3 import Error

# Code Inspiration: https://www.excelcise.org/python-sqlite-insert-data-pandas-data-frame/

DB_FILE_PATH = 'movieratings.db'
CSV_FILE_PATH = 'movies.csv'

def connect_to_db(db_file):
    """
    Connect to SQlite database and return a sqlite3 connection
    """
    sqlite3_conn = None

    try:
        sqlite3_conn = sqlite3.connect(db_file)
        return sqlite3_conn

    except Error as err:
        print(err)

        if sqlite3_conn is not None:
            sqlite3_conn.close()

def get_column_names_from_db_table(sql_cursor, table_name):
    """
    Scrape and return the column names from a table into a list
    """

    table_column_names = 'PRAGMA table_info(' + table_name + ');'
    sql_cursor.execute(table_column_names)
    table_column_names = sql_cursor.fetchall()

    column_names = list()
    for name in table_column_names:
        column_names.append(name[1])

    return column_names

def insert_values_to_table(table_name, csv_file):
    """
    1. Open csv file with pandas
    2. Store data into a pandas dataframe
    3. Add table's column names as data frame headers
    4. Insert data into table
    """

    conn = connect_to_db(DB_FILE_PATH)

    if conn is not None:
        c = conn.cursor()
        df = pd.read_csv(csv_file)

        ###############################################
		# reshape original data to match table schema #
		###############################################
        df = df[['title','year','plot','genre','rating','numvotes']] # reorder columns
        df.reset_index(inplace=True) # add unique id column

        df.columns = get_column_names_from_db_table(c, table_name)

        df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

        conn.close()
        print('SQLite Data Import Complete')
    else:
        print('Connection to Database Failed')

if __name__ == '__main__':
    insert_values_to_table('Movies', CSV_FILE_PATH)
