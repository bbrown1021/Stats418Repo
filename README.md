# UCLA Masters of Applied Statistics - Stats 418

Britney Brown (505-119-082)

# Problem Set 2

## Question 1 and 2

Inside the hw2 directory, run ```sqlite3 < create_tables.sql``` to create a local database ***movieratings.db***. To populate the *Movies* table in this database, run ```python3 populate.py``` to read in the given *movies.csv* file and import the data. Finally, run ```sqlite3 < queries.sql``` to print the counts of movies with at least 1000 votes. The resulting query is:  

![](hw2/screenshots/query_result.png?raw=true "Query Result")

When it comes to the release year constraint for the *Movies* table, all movies are released between 1887 and 2021. This is because celluloid was developed as a base for photographic emulsions in 1887 by Hannibal Goodwin, forever changing the motion-picture camera and the film industry as we know it. 

## Question 3

Using Terminal, navigate inside the **flask_app_code** directory and run  ```flask run```. 

There are two functionalities on this API:  

**1) Search for a Movie.**  

When a user searches for a movie title, the API will return a XML output of various film attributes as well as the official movie poster if and only if the movie exists in the Top 250 database. Please note that this search is case and spelling sensitive. The following is an example search of the "The Dark Knight" film.
		
![](hw2/screenshots/TheDarkKnight.png?raw=true "Example Movie Search")

**2) Submit a Rating for a Movie.**   

User can insert a username, movie title, and rating (integer from 1 to 10). The site will return an error code to help users adjust their ratings if they are invalid. This information will be saved and added to the *Users* and *Ratings* tables in ***movieratings.db***. To view the new users and ratings in the ***movieratings.db***, navigate to the **hw2** directory and run ```sqlite3 < check.sql```. Below is an example where two new users, Josie and Joe Bruin, rate a few movies.  

![](hw2/screenshots/question3_ex_tables.png?raw=true "User and Rating Table Examples")


## Question 4 

To create the scatterplot and barchart shown below, run ```python3 plots.py``` to create ***matplotlib_plot.png***. 

### Matplotlib 
![](hw2/matplotlib_plot.png?raw=true "Matplot Graph")

## Extra Credit

### Plotly (Extra Credit 2)

A similar graphic can be viewed at the following: ***plotly_dashboard.html***. Users can scroll through the graph to retrieve details for specific release years.  

![](hw2/screenshots/scatterplot.png?raw=true "Plotly Scatterplot")
![](hw2/screenshots/barchart.png?raw=true "Plotly Bar Chart")

### Third Party API (Extra Credit 5)  

In the **extra_credit** directory, run ```python3 app.py```. This will open a movie search using OMDB's API as well as a free API, QRcode Monkey. On this page, a user can type in any movie title (Note: this search is not case or spelling sensitive like the flask app in question 3). 

![](hw2/screenshots/extra/search_screen.png?raw=true "Initial Search Screen")

After submitting a movie title, the app will connect to the OMDB API and retrieve posters of all movies that match the search.  

![](hw2/screenshots/extra/search_result.png?raw=true "Example Search Result")

Once a user locates the movie of interest, clicking on the poster will bring them to a JSON file listing various information such as release year, genre, plot, and more. 

![](hw2/screenshots/extra/json_info.png?raw=true "Example Additional JSON Information")

In addition to this detailed movie JSON, the API will also save an QR code image to the user's machine. Scanning the code will open a JSON of the movie details on their phone. 

![](hw2/sextra_credit/SearchResultQR.png?raw=true "Example QR Code")


# Problem Set 1

### Segment 1

A screenshot of this repository's gitignore can be found in the q1 directory. 

**Bonus question:** In theory, branching off the ```hw1``` branch for each individual segment q1, q2, etc. would allow for the commits of each branch and corresponding question to appear in order when merged back onto the hw1 branch.  

### Segment 2

The 'Hello World' Flask project is deployed here: http://stats418hello505119082world.azurewebsites.net/. The app code can be found in q2 along with the submodule used to deploy to Azure. 

### Segment 3

After installing VirtualBox 6.1 on my Mac OS, I then setup a Linux environment using the latest LTS version of Ubuntu. 

![](hw1/q3/VirtualBox_screenshot.png?raw=true "VirtualBox_setup")
![](hw1/q3/screenshot.png?raw=true "Linux_environment"). 

In the Linux command line, ```./setup.sh``` will install all necessary packages. A copy of this script can be found in q3 directory. 

### Segment 4

Inside q4 directory, **Command Line:**  
``` python3 main.py```

**Output:**
- successful connection to SQL database  
- successful transformation into pandas dataframe  
- **Answers:**  
4.1 - Store 2  
4.2 - 2017-11-07  
4.3 - 2019  
4.4 - Store 2  
4.5 - Store 7   
- successful creation of new csv file in q4 directory
- successful creation of plot in q4 directory

### Segment 5

***Section 5.1***  
``` df_reshape.py``` reshapes the original ```TV-Sales.csv``` file  into ``` clean_TV_sales.csv``` to match the sales schema defined in ```create.sql```

Inside q5 directory, **Command Line:**  
``` python3 df_reshape.py```  
``` sqlite3 < create.sql```

**Output:**
- db.sqlite3 database in the hw1 directory

***Section 5.2-5***  
Inside q5 directory, **Command Line:**
``` sqlite3 < queries.sql```

**Output:**
- schema for stores table
- schema for sales table
- **Answers:**  
5.2 - Store 2   
5.3 Stores 8, 9, and 10   
5.4 -  Store 2  
5.5 - 37th week of the year   

### Segment 6  

```main.py``` utilizes the example input 2D arrays found in ```data.py``` which can be opened and customized by user

Inside q6 directory, **Command Line:**  
``` python3 main.py```

**Output:**  
- all numpy arrays for the main assignment
- all numpy arrays for the ***bonus assignments*** including
  - a new file ```input_array.npy``` of the current example array in q6 directory

## Extra Credit

### Segment 7

Due to my music background, I chose the following Kaggle dataset (https://www.kaggle.com/vageeshabudanur/songdetails) which contains songs from the 1990-2010 top 10 of the Billboard Hot 100 as well as songs that did not make the list (for comparison). Some variables include artist, time signature, loudness, key, pitch, tempo, and timbre. In the q7 directory, you will find the data under ```songs.csv``` and an extensive EDA in the notebook ```musicEDA.ipynb```.

### Segment 8

Navigate to the q8 directory for the TV sales analysis performed in R which includes all questions/queries from segments 4 and 5, as well as the bonus plot from segment 4. The notebook can be viewed at ```R_extra_credit.Rmd``` and the rendered document is viewable at ```R_extra_credit.pdf```. Note that a dataset with imputed missing values was generated under the name ```repaired.csv``` and the extra credit plot is saved at ```extra_plot.jpeg``` as well.
