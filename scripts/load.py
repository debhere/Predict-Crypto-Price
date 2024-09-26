from sqlalchemy import create_engine
from transform import transform

def load():
    server='DESKTOP-OKR44CT'
    Database = '70-461'
    Driver = 'ODBC driver 17 for SQL Server'
    conn_string = f'mssql://@{server}/{Database}?driver={Driver}'

    #engine = create_engine('mssql+pyodbc://DESKTOP-OKR44CT/Deb/70-461')
    engine = create_engine(conn_string)
    connection = engine.connect()
    raw = transform()
    raw.to_sql(name = "coinbasebtcpricerawdata", con = connection, schema = "staging", 
               if_exists = "append", index = False)


if __name__ == "__main__":
    load()
