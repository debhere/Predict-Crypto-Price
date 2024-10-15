CREATE DATABASE crypto

GO

CREATE SCHEMA staging

GO

----creating raw and rawhistory tables----

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


DROP TABLE IF EXISTS productcandles
CREATE TABLE productcandles(
	lowprice decimal(10, 2),
	highprice decimal(10, 2),
	openprice decimal(10, 2),
	closeprice decimal(10, 2),
	volume decimal(10, 2),
	tickdatetime datetime,
	product nvarchar(10)
)

/****** Procedure:  Transmit data from raw to rawhistory table ******/

IF OBJECT_ID('staging.sp_rawtorawhistory', 'P') is not null
	DROP PROC staging.sp_rawtorawhistory
GO
CREATE PROC staging.sp_rawtorawhistory AS
BEGIN
	BEGIN TRY
		INSERT INTO staging.coinbasebtcpricerawhistory
			SELECT * FROM staging.coinbasebtcpriceraw t1
			WHERE NOT EXISTS
			(
				SELECT * FROM staging.coinbasebtcpricerawhistory t2
				WHERE t1.ticktimestamp = t2.ticktimestamp
			)

		INSERT INTO staging.coinbasethpricerawhistory
			SELECT * FROM staging.coinbasethpriceraw t1
			WHERE NOT EXISTS
			(
				SELECT * FROM staging.coinbasethpricerawhistory t2
				WHERE t1.ticktimestamp = t2.ticktimestamp
			)

		delete from staging.coinbasebtcpriceraw
		delete from staging.coinbasethpriceraw
		RETURN 0
	END TRY
	BEGIN CATCH
		SELECT ERROR_MESSAGE() AS ErrorMessage, ERROR_NUMBER() AS ErrorNumber,
		ERROR_LINE() AS ErrorLine
		RETURN 1
	END CATCH	
END

GO

/****** Procedure:  Transmit data from staging to main ******/

IF OBJECT_ID('sp_stagingtomain', 'P') is not null
	DROP PROC sp_stagingtomain
GO
CREATE PROC sp_stagingtomain AS
BEGIN
	BEGIN TRY
		INSERT INTO productcandles
		 SELECT * FROM 
			(SELECT lowprice, highprice, openprice, closeprice, volume, tickdatetime, product
			FROM staging.coinbasebtcpricerawhistory
			UNION
			SELECT lowprice, highprice, openprice, closeprice, volume, tickdatetime, product
			FROM staging.coinbasethpricerawhistory)T ORDER BY tickdatetime, product
			RETURN 0
	END TRY
	BEGIN CATCH
		SELECT ERROR_MESSAGE() AS ErrorMessage, ERROR_NUMBER() AS ErrorNumber,
		ERROR_LINE() AS ErrorLine
		RETURN 1
	END CATCH
END
GO