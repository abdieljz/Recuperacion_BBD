--ZAMBRANO JUNIOR
--CREACION DE BASE DE DATOS 
--CREACION DE TABLAS


CREATE TABLE DIRECCION (
    Num_Direccion     INTEGER      PRIMARY KEY,
    Detalle_Direccion VARCHAR (50),
    Id_Emple          INTEGER      REFERENCES EMPLEADO (Id_Emple) 
);

CREATE TABLE EMPLEADO (
    Id_Emple           INTEGER      PRIMARY KEY,
    Num_Asig           VARCHAR (50),
    Fecha_Presentación DATE,
    Tipo                            REFERENCES PROCESO (Tipo) 
);
CREATE TABLE LUGAR (
    Block         INTEGER,
    Lot,
    Num_Direccion         REFERENCES DIRECCION (Num_Direccion) 
);
CREATE TABLE PERMISO (
    Estado        VARCHAR (50) PRIMARY KEY,
    Fecha_permiso DATE,
    Tipo          VARCHAR (50) REFERENCES PROCESO (Tipo) 
);
CREATE TABLE PROCESO (
    Tipo                INTEGER      PRIMARY KEY,
    Detalle_Tipo        VARCHAR (50),
    Fecha_Creacion_Tipo DATE,
    Estado              VARCHAR (50) REFERENCES PERMISO (Estado) 
);
