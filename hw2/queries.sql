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
.schema Movies
SELECT("------------------------------");

--  Print counts of movies with at least 1000 votes, grouped by their rating bin. 
--  All movies with the same integer part of rating fall in the same rating bin.

SELECT count(MovieTitle) as "Movies",
(cast ( AverageRating as int ) - ( AverageRating < cast ( AverageRating as int ))) as "RatingBin"
FROM Movies
WHERE NumberOfVotes > 1000
GROUP By RatingBin
;