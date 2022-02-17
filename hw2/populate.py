import pandas as pd
import numpy as np

# read in original
df = pd.read_csv('movies.csv')

# reorder data to fit movies schema
movies = df[['title','year','plot','genre','rating','numvotes']]

# add an id column
movies.reset_index(inplace=True)

# save as csv file
movies.to_csv('clean_movies.csv', index = False) 

