###########################
######### Settings ########
###########################
.header ON
.timer ON
.mode column 

###########################
### Connect to Database ###
###########################
.open ../db.sqlite3
.databases
.tables
.schema sales

-- select * from sales
-- limit 100;

-- SELECT  saleDate, 
--         (substr(saleDate,4,2) || '-' || substr(saleDate,7,4) || '-' || substr(saleDate,1,2)) as dateconverted,
--         strftime('%Y', (substr(saleDate,7,4) || '-' || substr(saleDate,4,2) || '-' || substr(saleDate,1,2)) ) as year
-- FROM sales
-- LIMIT 10;

SELECT saleDate,strftime('%Y',saleDate) as "Year",
strftime('%m',saleDate) as "Month",
strftime('%d',saleDate) as "Day"
FROM sales
LIMIT 10;

-- select distinct YEAR(saleDate)-- count(*)
-- from sales
-- limit 100

-- ;

# 5.2	Which store makes the maximum sales on Sundays?
-- select 
-- 	sum(S1) as s1_sales
--     , sum(s2) as s2_sales
--     , sum(s3) as s3_sales
--     , sum(s4) as s4_sales
--     , sum(s5) as s5_sales
--     , sum(s6) as s6_sales
--     , sum(s7) as s7_sales
--     , sum(s8) as s8_sales
--     , sum(s9) as s9_sales
--     , sum(s10) as s10_sales
-- from sales
-- where DAYOFWEEK(Date) = 1
-- limit 100
-- ;

# 5.3	Find all stores with total sales in December lower than those of S5.

# 5.4	Which store recorded the highest number of sales for the largest number of days?

# 5.5	What week in 2019 has the highest total sales across all the stores?



-- SELECT DISTINCT saleDate, sale, name FROM sales
-- INNER JOIN stores
-- ON stores.storeId = sales.store
-- WHERE NULLIF(sale, 'N/A') IS NOT NULL
-- AND sale > 80;