CREATE DATABASE crypto

GO

CREATE SCHEMA staging

GO

IF OBJECT_ID('U', 'coinbasebtcpricerawdata') IS NOT NULL
	DROP TABLE staging.coinbasebtcpricerawdata
CREATE TABLE staging.coinbasebtcpricerawdata(
	TickTimestamp BigInt,
	LowPrice decimal(10, 2),
	HighPrice decimal(10, 2),
	OpenPrice decimal(10, 2),
	ClosePrice decimal(10, 2),
	Volume decimal(10, 2),
	TickDateTime datetime,
	product nvarchar(10)
)