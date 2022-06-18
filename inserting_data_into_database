import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


#Connecting with my local database using user name, password
engine = create_engine('mysql://username:password@localhost')

"""
Connection is prefered for executing sql queries as it gives 
greater control over attributes of the connection  
"""
connection = engine.connect()
connection.execute("CREATE DATABASE IF NOT EXISTS betme")
connection.execute("USE betme")
connection.execute("DROP TABLE IF EXISTS football")

#SQL query for table creation
sql_com = """ CREATE TABLE football
               (
               `index`      INT(20)       UNIQUE PRIMARY KEY AUTO_INCREMENT,
               `Div`        VARCHAR(20)   NOT NULL,
               `DateTime`   DATETIME      NOT NULL,
               `HomeTeam`   VARCHAR(20)   NOT NULL,
               `AwayTeam`   VARCHAR(20)   NOT NULL,
               `FTHG`        INT          DEFAULT 0,
               `FTAG`        INT          DEFAULT 0
               )
               """
