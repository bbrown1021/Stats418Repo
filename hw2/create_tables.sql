# create database
.open movieratings.db
.databases

# create movies table
CREATE TABLE IF NOT EXISTS Movies (
	MovieId INTEGER PRIMARY KEY,
	MovieTitle TEXT,
	ReleaseYear INTEGER CHECK (ReleaseYear < 2021 and ReleaseYear > 1887),
	PlotDescription TEXT,
	Genre TEXT,
	AverageRating DECIMAL (3,1) CHECK (AverageRating >= 1.0 and AverageRating <= 10.0), --set 3 for precision in case of 10.0 and only allow one digit after decimal
	NumberOfVotes INTEGER
);

# populate movies table
DELETE FROM "Movies"; -- verify table is empty
.mode csv
.import clean_movies.csv Movies --skip 1

# create users table
CREATE TABLE IF NOT EXISTS Users (
	UserId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	Username TEXT,
	FirstName TEXT,
	LastName TEXT
);

# create ratings table
CREATE TABLE IF NOT EXISTS Ratings (
	RatingId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	UserId INTEGER,
	MovieId INTEGER,
	Rating INTEGER CHECK (Rating >= 1 and Rating <= 10), --whole number between 1 and 10
	FOREIGN KEY(UserId) REFERENCES Users(UserId),
	FOREIGN KEY(MovieId) REFERENCES Movies(MovieId)
);