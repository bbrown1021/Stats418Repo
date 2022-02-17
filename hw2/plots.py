import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.pyplot
import matplotlib.dates
import numpy as np
import pandas as pd
import scipy.stats as st

## Question 4:
# Using movies.csv and matplotlib to draw a bar graph showing the number of movies each year that were in the Top 250 dataset. 
# Also, plot the average ratings of movies in each year as a scatter plot on top of that. 
# For each point in the scatter plot, add error bars corresponding to 95% intervals. 
# Assume that the rating of each movie for a particular year is a Guassian distribution with known σ=1. 
# If a particular year does not have films, have an empty spot corresponding to that year. 
# Add xticks at intervals of 5 years with vertical labels, and yticks at each integer from 1 to 10. 
# Also, add a horizontal grid with unit separation. Add a dashed red horizontal line corresponding to the mean of all 250 movies.

# read in data
df = pd.read_csv('movies.csv')

# summarise data for graph
df_subset = df[['title','year','rating']]
df_group = df_subset.groupby('year')
moviecount = pd.DataFrame(df_group['title'].count()) # number of movies per year
avgratings = df_group.mean('rating') # average rating of each year
df2 = pd.concat([moviecount,avgratings], axis = 1)
df2.reset_index(inplace = True)

# get the 95% confidence interval of the mean
years = sorted(df_subset['year'].unique())
rows = []
for x in years:
    data = df_subset[df_subset['year'] == x]['rating']
    dd = pd.DataFrame(data).to_numpy()
    
    # case 1: only one movie for that year 
    if len(data) == 1:
        tup = (data.iloc[0],data.iloc[0])
        rows.append(tup)
        
    # case 2: multiple movies with the same rating
    elif np.all(dd == dd[0]) == True:
        tup = (data.iloc[0],data.iloc[0])
        rows.append(tup)
        
    # case 3: multiple movies with different ratings    
    else:
        interval = st.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data))
        rows.append(interval)

# save summerised info as dataframe
intervals = pd.DataFrame(rows, columns=["lower", "upper"])
df2 = pd.concat([df2,intervals], axis = 1)
df2["error"] = (intervals['upper'] - intervals['lower'])/2

# define plot
fig, (ax1, ax2) = plt.subplots(2, figsize = (18,10))
year_ticks = pd.Series(np.arange(1920,2021,5))

# bar graph showing the number of movies each year that were in the Top 250 dataset
ax2.bar(df2['year'], df2['title'])
ax2.set(xlabel = 'Year', ylabel='Number of Top 250 Movies')
ax2.set_xticks(year_ticks)
ax2.set_yticks(pd.Series(np.arange(0,11,1)))
ax2.grid(which='both', axis = "y")

# plot the average ratings of movies in each year as a scatter plot (on top)
# add error bars corresponding to 95% intervals (calculated above)
ax1.errorbar(df2['year'], df2['rating'], yerr=df2['error'], fmt="o", color = 'orange')
ax1.set( ylabel='Average Rating of Top 250 Movies')
ax1.set_xticks([])
ax1.set_yticks(pd.Series(np.arange(4,15,1)))
ax1.grid(which='both', axis = "y")

# dashed red horizontal line corresponding to the mean of all 250 movies
ax1.axhline(y = df2['rating'].mean(), color = 'r', linestyle = 'dashed') 

# save figure 
fig.tight_layout()
plt.savefig('matplotlib_plot.png')


## Extra Credit 2
# Create the plot described in Question 4 using only plotly.
import plotly
import plotly.express as px

fig1 = px.scatter(df2, y="rating", x="year", error_y="error",
                 labels={"year": "Year",
                        "rating": "Average Rating of Top 250 Movies"})
fig1.update_traces(marker={'size': 10})
fig1.add_hline(y=df2['rating'].mean(), line_dash="dash", line_color="red")

fig1.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        dtick = 5,
        tickangle = 90
    ),
    yaxis = dict(
        tickmode = 'linear',
        dtick = 1,
    )
)

fig2 = px.bar(df2, x='year', y='title',
             labels={"year": "Year",
                     "title": "Number of Top 250 Movies"
                 })

fig2.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 100,
        dtick = 5,
        tickangle = 90
    )
)

def figures_to_html(figs, filename="plotly_dashboard.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
figures_to_html([fig1, fig2])
