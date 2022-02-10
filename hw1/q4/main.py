"""
Segment 4
Use the same dataset as segment 5 for this question. 
Connect to your sqlite3 database with Python and export your data into a pandas DataFrame.

Write a pandas program (hw1/q6/main.py) that outputs the answers to the following queries, one per line:
4.1	Which store had the highest mean sale in 2017?
4.2	Which day showed the highest variance in sales across different stores?
4.3	Which year showed the highest median sale for the store S5?
4.4	Which store recorded the highest number of sales for the largest number of days?
4.5	Which store ranks 5th in the cumulative number of units sold over the 3-year interval?
4.6	Your program should create a file named repaired.csv in the directory hw1/q4 which contains the same data as TV-Sales.csv, but with “N/A” values replaced with the median sale of that store, over the entire 3-year interval. Retain the header row found in TV-Sales.csv.
"""

# -------------------------------- #
# Import Modules
# -------------------------------- #
from datetime import datetime
import logging
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot
import matplotlib.dates
import numpy as np
import sqlite3

# -------------------------------- #
# Set up Logging
# -------------------------------- #
logging.basicConfig(level=logging.INFO)  # basic configuration
LOGGER = logging.getLogger(__name__)  # define one logger for current file

# -------------------------------- #
# Connect to SQL
# -------------------------------- #
print("----------------------------------------------------------")
conn = sqlite3.connect('../db.sqlite3')
print("Successfully Connected to SQL Database:")

# # -------------------------------- #
# # Export Data into Pandas DataFrame
# # -------------------------------- #
df_sql = pd.read_sql('SELECT saleDate,sale,name FROM sales INNER JOIN stores ON stores.storeId = sales.store ', conn)
print(df_sql)
print("----------------------------------------------------------")
print("Successfully Export Data into Pandas Dataframe:")
df2 = df_sql.pivot(index = 'saleDate', columns = 'name', values = 'sale').reset_index()
df2.rename(columns={'saleDate': 'Date'}, inplace=True)
df1 = df2[["Date","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10"]]
df = pd.read_csv('TV-Sales.csv')
print(df)
# make Date column into 'datetime' type
df['Date'] = pd.to_datetime(df['Date'])

# create new columns for day/month/year
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year
# print(df.head(10)) # view data

df_stores = df.iloc[:,1:11]

# -------------------------------- #
# Begin Assignment
# -------------------------------- #


def get_answer1():
	print("Part 4.1 -------------------------------------------------")

	# subset to year 2017
	df_2017 = df[df['year']==2017]

	# find means of store and choose id of maximum value
	print(f'The store with the highest mean sale in 2017: {df_2017.iloc[: , 1:11].mean().idxmax()} ') # store associated with highest mean sale

def get_answer2():
	print("Part 4.2 -------------------------------------------------")

	orig_dates = pd.read_csv('TV-Sales.csv')
	print(f'The highest variance, {round(orig_dates.iloc[: , :11].var(axis=1).max(),2)}, occurs on the date: {orig_dates.iloc[orig_dates.iloc[: , :11].var(axis=1).idxmax(),0]}. ')

def get_answer3():
	print("Part 4.3 -------------------------------------------------")

	df5_max_median = df[['S5','year']].groupby(['year']).median().idxmax()
	print(f"Store 5 had the highest median sale in the year: {int(df5_max_median)}") 

def get_answer4():
	print("Part 4.4 -------------------------------------------------")

	a_list = []
	for i in range(df_stores.shape[0]):
	    a_list.append(df_stores.iloc[i,:].idxmax())

	# returns a dictionary of each store's count of highest sales
	unique, counts = np.unique(a_list, return_counts=True)
	store_count_dict = dict(zip(unique, counts))
	
	print(f"The store with the highest number of sales for the largest number of days: {max(store_count_dict, key=store_count_dict.get)} ") 

def get_answer5():
	print("Part 4.5 -------------------------------------------------")

	df_cum = pd.DataFrame(df_stores.sum()) # sum of sales per store
	df_cum.columns = ['value']
	sorted_values = df_cum.sort_values(by=['value'], ascending=False)
	print(f"The store that ranks 5th in the cumulative number of units sold over three years: {list(sorted_values.index)[4]}") 

def get_answer6():
	print("Part 4.6 -------------------------------------------------")

	store_medians = df_stores.median() # median sale for each store
	values = store_medians.to_dict() # store values in dictionary format
	df_new = df.fillna(value=values) # replace NAN with median value dictionary above
	df_new = df_new.iloc[:,range(11)] # only original columns
	df_new.isnull().values.any() # check if NAN exist

	df_new.to_csv('repaired.csv', index = False) # create new csv file
	print(f'New file (repaired.csv) has been created.')

get_answer1()
get_answer2()
get_answer3()
get_answer4()
get_answer5()
get_answer6()

def bonus():
	print("Bonus -------------------------------------------------")

	data = pd.read_csv('repaired.csv')
	x_values = data.iloc[:,:1]
	dates = matplotlib.dates.date2num(x_values)

	y_values = data.iloc[:,1:].cumsum()
	S1 = y_values.iloc[:,0]
	S2 = y_values.iloc[:,1]
	S3 = y_values.iloc[:,2]
	S4 = y_values.iloc[:,3]
	S5 = y_values.iloc[:,4]
	S6 = y_values.iloc[:,5]
	S7 = y_values.iloc[:,6]
	S8 = y_values.iloc[:,7]
	S9 = y_values.iloc[:,8]
	S10 = y_values.iloc[:,9]

	y_min = 0
	y_max = y_values.max(axis=1).max()

	x_min = dates.min()
	x_max = dates.max()

	fig, ax = plt.subplots(figsize = (20,12))

	ax.plot(dates, S1, label = "S1", linewidth = 0.8)
	ax.plot(dates, S2, label = "S2", linewidth = 0.8)
	ax.plot(dates, S3, label = "S3", linewidth = 0.8)
	ax.plot(dates, S4, label = "S4", linewidth = 0.8)
	ax.plot(dates, S5, label = "S5", linewidth = 0.8)
	ax.plot(dates, S6, label = "S6", linewidth = 0.8)
	ax.plot(dates, S7, label = "S7", linewidth = 0.8)
	ax.plot(dates, S8, label = "S8", linewidth = 0.8)
	ax.plot(dates, S9, label = "S9", linewidth = 0.8)
	ax.plot(dates, S10, label = "S10", linewidth = 0.8)

	ax.legend(bbox_to_anchor=(1.0, 0.8, 0.3, 0.2), loc='upper left')

	y_minor_tick = list(range(int(y_max)))[0::1000]
	ax.set_yticks(y_minor_tick, minor=True) # Grid

	x_ticks = list(dates.tolist())[0::90]
	ax.set_xticks(x_ticks) # Grid

	ax.grid(which='both', alpha=1)

	plt.savefig('plot.png')


	print(f'New file (plot.png) has been created.')

bonus()
