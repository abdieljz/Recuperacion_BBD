import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from datetime import datetime
import psycopg2

def log(logfile, message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(logfile,"a") as f: 
        f.write('[' + timestamp + ']: ' + message + '\n')
        print(message)

def transform():

    log(logfile, "-------------------------------------------------------------")
    log(logfile, "Inicia Fase De Transformacion")
    df = pd.read_csv('Building_Permits.csv')
    df_empleado = pd.read_sql_query("""

        SELECT Record ID AS Id_Emple, 
        Permit Number AS Num_Asig,
        Filed Date AS Fecha_Presentacion
        FROM buildingpermits 
     
        """, con=engine.connect())

    df_empleado.columns = ['Record ID', 'Permit Number', 'Permit Type']
    
   
    df_lugar= pd.read_sql_query("""

        SELECT BlocK , 
        Lot ,
        FROM buildingpermits

    """ , con=engine.connect())

    df_lugar.columns = ['Num_Direccion', 'Detalle_Direccion']

    df_lugar = pd.read_sql_query("""

        SELECT Street Number AS AS Num_Direccion,
        Street Name AS Detalle_Direccion, a.Id_Emple 
        FROM buildingpermits
        INNER JOIN df_empleado ON df_empleado.Permit Number = buildingpermits.Permit Number

      
    """ , con=engine.connect())

    df_lugar.columns = ['Num_Direccion', 'Detalle_Direccion']

    df_proceso = pd.read_sql_query("""

        SELECT AS TIPO
        Current Status AS Detalle_Tipo
        Current Status Date AS Fecha_Creacion_Tipo, a.estado
        FROM buildingpermits
        inner join df_empleado on df_empleado.Permit Number = buildingpermits.Permit Number

    """ , con=engine.connect())

    df_proceso.columns = ['Tipo', 'Detalle_Tipo', 'Fecha_Creacion_Tipo']
    
    df_permiso = pd.read_sql_query("""

    SELECT AS TIPO
        Current Status AS Detalle_Tipo
        Current Status Date AS Fecha_Creacion_Tipo,
        FROM buildingpermits
        
    
    """ , con=engine.connect())



    log(logfile, "-------------------------------------------------------------")

   
    log(logfile, "Finaliza Fase De Transformacion")
    log(logfile, "-------------------------------------------------------------")
    return df_empleado, df_lugar, df_proceso, df_permiso
   
def load():
    """ Connect to the PostgreSQL database server """
    conn_string = 'postgresql://postgres:172164@localhost/PERMISOS.db'
    db = create_engine(conn_string)
    conn = db.connect()
    try:
        log(logfile, "-------------------------------------------------------------")
        log(logfile, "Inicia Fase De Carga")
        df_empleado.to_sql('df_empleado', con=db, if_exists='replace', index=False)
        df_lugar.to_sql('df_lugar', con=db, if_exists='replace', index=False)
        df_proceso.to_sql('df_proceso', con=db, if_exists='replace', index=False)
        df_permiso.to_sql('df_permiso', con=db, if_exists='replace', index=False)
        log(logfile, "Finaliza Fase De Carga")
        log(logfile, "-------------------------------------------------------------")
        conn = psycopg2.connect(conn_string)
        conn.autocommit = True
        cursor = conn.cursor()
        log(logfile, "Finaliza Fase De Carga")
        log(logfile, "-------------------------------------------------------------")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally: 
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def extract():
    log(logfile, "--------------------------------------------------------")
    log(logfile, "Inicia Fase De Extraccion")
    metadata = MetaData()
    metadata.create_all(engine)
    log(logfile, "Finaliza Fase De Extraccion")
    log(logfile, "--------------------------------------------------------")


if __name__ == '__main__':
    
    logfile = "ProyectoETL_logfile.txt"
    log(logfile, "ETL Trabajo iniciado.")
    engine = create_engine('sqlite:///PERMISOS.db')
    extract()
    (df_empleado, df_lugar, df_proceso, df_permiso) = transform()
    load()
    log(logfile, "ETL Trabajo finalizado.")
