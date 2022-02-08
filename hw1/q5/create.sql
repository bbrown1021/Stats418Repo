# create database
.open db.sqlite3
.databases

.headers ON

# create store table
CREATE TABLE IF NOT EXISTS stores (
	storeId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name TEXT
);

# insert data into store table
INSERT INTO stores(name) VALUES('S1');
INSERT INTO stores(name) VALUES('S2');
INSERT INTO stores(name) VALUES('S3');
INSERT INTO stores(name) VALUES('S4');
INSERT INTO stores(name) VALUES('S5');
INSERT INTO stores(name) VALUES('S6');
INSERT INTO stores(name) VALUES('S7');
INSERT INTO stores(name) VALUES('S8');
INSERT INTO stores(name) VALUES('S9');
INSERT INTO stores(name) VALUES('S10');

# create sales table
CREATE TABLE IF NOT EXISTS sales (
	saleId INTEGER PRIMARY KEY AUTOINCREMENT,
	saleDate DATE,
	sale INTEGER,
	store INTEGER,
	FOREIGN KEY(store) REFERENCES stores(storeId)
);

# verify sales table is empty
DELETE FROM "sales";

# read in table from cleaned csv
.mode csv
.import clean_TV_sales.csv sales --skip 1
