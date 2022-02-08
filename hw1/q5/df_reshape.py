import pandas as pd
import numpy as np

# read in original
df = pd.read_csv('TV-Sales.csv')

# renmae columns to be the foreign key
df.rename(columns={'S1': '1', 
                   'S2': '2',
                   'S3': '3',
                   'S4': '4',
                   'S5': '5',
                   'S6': '6',
                   'S7': '7',
                   'S8': '8',
                   'S9': '9',
                   'S10': '10'}, 
                   inplace=True)

# reshape data wide to long
df2 = pd.melt(df,id_vars=['Date'],var_name='store', value_name='sale')

# add salesId and rename values
df2.reset_index(inplace=True)
df2 = df2[["index","Date","sale","store"]]
df2.rename(columns={'index': 'saleId', 'Date': 'saleDate'}, inplace=True)

# save df as csv file
df2.to_csv('clean_TV_sales.csv', index = False) 