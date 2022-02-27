import requests
import sqlalchemy as db
import pandas as pd

def match_query(title):
	"""
	Returns XML object from OMDB API if movie search matches title in top 250 movieratings.db
	"""

	####################
	# SQL Alchemy
	####################

	# create connection to sqlite database
	engine = db.create_engine('sqlite:///../movieratings.db')
	connection = engine.connect()
	metadata = db.MetaData()

	# establish table object
	Movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

	# extract matching movie
	query = db.select([Movies.columns.MovieTitle, Movies.columns.ReleaseYear]).where(Movies.columns.MovieTitle == title)
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()

	if ResultSet: # exists
		
		####################
		# OMDB API
		####################

		# match OMDB to sqlite database
		apiKey = '36921cd1'
		data_URL = 'http://www.omdbapi.com/?apikey='+apiKey

		movieTitle = ResultSet[0][0]
		year = ResultSet[0][1]

		params = {
		    's':movieTitle,
		    'type':'movie',
		    'y':year    
		}

		# fetch movie data
		response = requests.get(data_URL,params = params).json() #dict


		if (response['Response']=='True'):
			imdbID = response['Search'][0]['imdbID']
			poster = response['Search'][0]['Poster']

			# return XML from matched OMDB
			params2 = {
			    'i':imdbID,
			    'plot':'short',
			    'r':'xml'   
			}

			response2 = requests.get(data_URL,params = params2)
			xml_result = response2.text 
			return [xml_result, poster]
			
		else:
			return ['<root response="False"><error>404 Error. Movie Not Found</error></root>', 'https://cdn2.vectorstock.com/i/1000x1000/87/16/404-error-with-character-error-design-template-vector-20568716.jpg']

	else:
		return ['<root response="False"><error>404 Error. Movie Not Found</error></root>', 'https://cdn2.vectorstock.com/i/1000x1000/87/16/404-error-with-character-error-design-template-vector-20568716.jpg']

def rate_movie(username, movie, rating):

	valid_ratings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	if not rating in valid_ratings:
		return f'<root response="False"><error>Invalid Input Error: Rating {rating} is not a valid response. Please input a rating between 1 and 10</error></root>'

	# create connection to sqlite database
	engine = db.create_engine('sqlite:///../movieratings.db')
	connection = engine.connect()
	metadata = db.MetaData()

	# establish table objects
	Movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)
	Users = db.Table('Users', metadata, autoload=True, autoload_with=engine)
	Ratings = db.Table('Ratings', metadata, autoload=True, autoload_with=engine)


	# check if user exists
	query = db.select([Users.columns.Username]).where(Users.columns.Username == username)
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()

	# creates user if does not exist
	if not ResultSet:
		print(f'user {username} does not exist --creating user account')
		query = db.insert(Users).values(Username = username, FirstName = username, LastName = '') 
		ResultProxy = connection.execute(query)

	# extract user ID
	query = db.select([Users.columns.UserId]).where(Users.columns.Username == username)
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	user_id = int(str(ResultSet[0]).replace('(','').replace(',)',''))
	print(user_id)
	print(type(user_id))

	# check if movie exists 
	query = db.select([Movies.columns.MovieId]).where(Movies.columns.MovieTitle == movie)
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	movie_id = int(str(ResultSet[0]).replace('(','').replace(',)',''))

	if not ResultSet: # exists
		return f'<root response="False"><error>404 Error. Movie {movie} Not Found</error></root>'

	# add rating to Ratings
	query = db.insert(Ratings).values(UserId = user_id, MovieId = movie_id, Rating = rating) 
	ResultProxy = connection.execute(query)

	return f'Your rating of {rating} for {movie} has been recorded.'
