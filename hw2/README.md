# UCLA Masters of Applied Statistics - Stats 418

Britney Brown (505-119-082)

# Problem Set 2

## Question 1 and 2

Inside the hw2 directory, run ```sqlite3 < create_tables.sql``` to create a local database ***movieratings.db***. To populate the *Movies* table in this database, run ```python3 populate.py``` to read in the given *movies.csv* file and import the data. Finally, run ```sqlite3 < queries.sql``` to print the counts of movies with at least 1000 votes. The resulting query is:  

![](screenshots/query_result.png?raw=true "Query Result")

When it comes to the release year constraint for the *Movies* table, all movies are released between 1887 and 2021. This is because celluloid was developed as a base for photographic emulsions in 1887 by Hannibal Goodwin, forever changing the motion-picture camera and the film industry as we know it. 

## Question 3

Using Terminal, navigate inside the **flask_app_code** directory and run  ```flask run```. 

![](screenshots/flask_home_page.png?raw=true "OMDB App Home Page")

There are two functionalities on this API:  

**1) Search for a Movie.**  

When a user searches for a movie title, the API will return a XML output of various film attributes as well as the official movie poster if and only if the movie exists in the Top 250 database. Please note that this search is case and spelling sensitive. The following is an example search of the "The Dark Knight" film.
		
![](screenshots/TheDarkKnight.png?raw=true "Example Movie Search")

**2) Submit a Rating for a Movie.**   

User can insert a username, movie title, and rating (integer from 1 to 10). The site will return an error code to help users adjust their ratings if they are invalid. This information will be saved and added to the *Users* and *Ratings* tables in ***movieratings.db***. To view the new users and ratings in the ***movieratings.db***, navigate to the **hw2** directory and run ```sqlite3 < check.sql```. Below is an example where two new users, Josie and Joe Bruin, rate a few movies.  

![](screenshots/question3_ex_tables.png?raw=true "User and Rating Table Examples")


## Question 4 

To create the scatterplot and barchart shown below, run ```python3 plots.py``` to create ***matplotlib_plot.png***. 

### Matplotlib 
![](matplotlib_plot.png?raw=true "Matplot Graph")

## Extra Credit

### Plotly (Extra Credit 2)

A similar graphic was also created in *plots.py* and can be viewed at the following dashboard: ***plotly_dashboard.html***. Users can scroll through the graph to retrieve details for specific release years.  

![](screenshots/scatterplot.png?raw=true "Plotly Scatterplot")
![](screenshots/barchart.png?raw=true "Plotly Bar Chart")

### Third Party API (Extra Credit 5)  

In the **extra_credit** directory, run ```python3 app.py```. This will open a different kind of movie search using OMDB's API as well as QRcode Monkey, a free API with documentation found at https://www.qrcode-monkey.com/qr-code-api-with-logo/. 

On this page, a user can type in any movie title (Note: this search is not case or spelling sensitive like the flask app in question 3). 

![](screenshots/extra/search_screen.png?raw=true "Initial Search Screen")

After submitting a movie title, the app will connect to the OMDB API and retrieve posters of all movies that match the search.  

![](screenshots/extra/search_result.png?raw=true "Example Search Result")

Once a user locates the movie of interest, clicking on the poster will bring them to a JSON file listing various information such as release year, genre, plot, and more. 

![](screenshots/extra/json_info.png?raw=true "Example Additional JSON Information")

In addition to this detailed movie JSON, the API will also save a QR code image to the user's machine. Scanning the code will open a JSON of the movie details on their phone. 

![](extra_credit/SearchResultQR.png?raw=true "Example QR Code")