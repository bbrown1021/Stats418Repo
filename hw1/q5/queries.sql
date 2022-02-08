###########################
######### Settings ########
###########################
.header ON
.mode column 

###########################
### Connect to Database ###
###########################
.open ../db.sqlite3
.databases
.tables
.schema stores
.schema sales

# 5.2	Which store makes the maximum sales on Sundays?
SELECT '-------------------------------------';

SELECT name as "Store", sum(sale) as "TotalSales"
FROM sales
INNER JOIN stores
ON stores.storeId = sales.store
WHERE strftime('%w',saleDate) = '0' -- sunday = 0 day of week
GROUP BY name
ORDER BY TotalSales desc
LIMIT 1
; 

-- ANSWER: S2

-- # 5.3	Find all stores with total sales in December lower than those of S5.
SELECT '-------------------------------------';

SELECT name as "Store", sum(sale) as "TotalSales"
FROM sales
INNER JOIN stores
ON stores.storeId = sales.store
WHERE strftime('%m', saleDate) = '12'
GROUP BY name
HAVING sum(sale) < (
	SELECT sum(sale)
	FROM sales
	WHERE store = 5 AND strftime('%m', saleDate) = '12')
ORDER BY TotalSales
;

-- ANSWER: S8, S9, S10

# 5.4	Which store recorded the highest number of sales for the largest number of days?
SELECT '-------------------------------------';

SELECT name, count(name) as 'HighestRecord'
FROM (
	SELECT name, saleDate, max(sale)
	FROM sales
	INNER JOIN stores
	ON stores.storeId = sales.store
	WHERE sale IS NOT NULL
	GROUP BY saleDate
	ORDER BY sale ASC
	)
GROUP BY name
ORDER BY HighestRecord DESC
LIMIT 1
;

-- ANSWER: S2


# 5.5	What week in 2019 has the highest total sales across all the stores?

SELECT strftime('%W',saleDate) as 'Week', sum(sale)
FROM sales
INNER JOIN stores
ON stores.storeId = sales.store
WHERE strftime('%Y',saleDate) = "2019"
GROUP BY Week
ORDER BY sum(sale) DESC
LIMIT 1
;

-- ANSWER: 37th week of the year


