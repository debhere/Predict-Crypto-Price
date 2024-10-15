CREATE DATABASE crypto

GO

CREATE SCHEMA staging

GO



DROP TABLE IF EXISTS staging.coinbasebtcpriceraw
CREATE TABLE staging.coinbasebtcpriceraw(
	ticktimestamp BigInt,
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)

DROP TABLE IF EXISTS staging.coinbasebtcpricerawhistory
CREATE TABLE staging.coinbasebtcpricerawhistory(
	ticktimestamp BigInt,
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)

DROP TABLE IF EXISTS staging.coinbasethpriceraw
CREATE TABLE staging.coinbasethpriceraw(
	ticktimestamp BigInt,
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)

DROP TABLE IF EXISTS staging.coinbasethpricerawhistory
CREATE TABLE staging.coinbasethpricerawhistory(
	ticktimestamp BigInt,
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)
