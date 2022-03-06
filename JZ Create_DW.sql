CREATE TABLE dim_Time (
    TimeId      VARCHAR (200)       NOT NULL
                             PRIMARY KEY,
    fecha      DATE          NOT NULL,
    año        INTEGER       NOT NULL,
    mes        INTEGER       NOT NULL,
    dia        INTEGER       NOT NULL,
    nombre_dia NVARCHAR (50) NOT NULL,
    dia_semana INTEGER       NOT NULL,
    semana     INTEGER       NOT NULL,
    trimestre  NVARCHAR (50) NOT NULL
);

CREATE TABLE dim_process (
    Id_process             INTEGER        PRIMARY KEY,
    CategoryName    varchar(8000) not null,
    ReorderLevel    INTEGER        NOT NULL,
    Discontinued    INTEGER        NOT NULL
);

CREATE TABLE dim_location (
    Id_location              INTEGER        PRIMARY KEY autoincrement  not null ,
    Address   varchar(60) NOT NULL,
    City       varchar(60) NOT NULL,
    Region      varchar(60) NOT NULL,
    PostalCode varchar(60) NOT NULL,
    Country    varchar(60) NOT NULL
    
);


CREATE TABLE dim_employee (
    Id_employe              INTEGER        PRIMARY KEY,
    LastName        VARCHAR (8000),
    FirstName       VARCHAR (8000),
    Title           VARCHAR (8000),
      
);

create table fact_Inventary (
    Id_Inventary varchar(8000) primary key  not null,
    id_customer  VARCHAR (8000),
    id_time      VARCHAR (200),
    Id_process   INTEGER,
    Id_location  INTEGER,
    Id_employee   INTEGER,
    Freight      DECIMAL        NOT NULL,
  
   
    REFERENCES dim_time (id_time) ON DELETE NO ACTION
                                      ON UPDATE NO ACTION, 
     FOREIGN KEY (
        Id_product
    )
    REFERENCES dim_product (Id_product) ON DELETE NO ACTION
                                      ON UPDATE NO ACTION,                                                                  
    FOREIGN KEY (
        Id_location
    )
    REFERENCES dim_location (Id_location) ON DELETE NO ACTION
                                      ON UPDATE NO ACTION, 
    FOREIGN KEY (
        Id_employe
    )
    REFERENCES dim_employee (Id_employe) ON DELETE NO ACTION
                                      ON UPDATE NO ACTION                                       
);