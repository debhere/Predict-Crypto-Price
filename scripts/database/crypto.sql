CREATE DATABASE crypto

GO

CREATE SCHEMA staging

GO


DROP TABLE IF EXISTS staging.coinbasebtcpricerawdata
CREATE TABLE staging.coinbasebtcpricerawdata(
	ticktimestamp BigInt,
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)