###########################
######### Settings ########
###########################
.header ON
.mode column 

###########################
### Connect to Database ###
###########################
.open movieratings.db
.databases
.tables
.schema Users
.schema Ratings

SELECT * FROM Users;
SELECT * FROM Ratings;