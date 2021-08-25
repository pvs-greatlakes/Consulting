# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:22:25 2020

@author: P.V.SUBRAMANIAN
"""
import mysql.connector
from   mysql.connector  import Error, errorcode
import random
import string

class Member:
      """
      In this Class object, we establish the data base connection, create MySQL tables and insert the 
      records for the following tables
      a. MEMBER

      
      """
    
      import mysql.connector
      from   mysql.connector  import Error, errorcode
      import random
      import string
    
      def  __init__(self, host, user, pwd, db):
           self.host     =   host
           self.db       =   db
           self.user     =   user
           self.pwd      =   pwd
           
      def db_connection(self):
          
    
           self.connection =  mysql.connector.connect(host  =  self.host,
                                              database =  self.db,
                                              user     =  self.user,
                                              password =  self.pwd)
           
           return  self.connection
       
      def db_create_table(self):
          
               
           # Drop table if it already exist using execute() method.
           connection  =   self.connection
           cursor      =   connection.cursor()
          # Create table as per requirement 
          
           cursor.execute("DROP TABLE IF EXISTS MEMBER")
           
           sql_member = """CREATE TABLE MEMBER(
                           PROFILE_ID                VARCHAR(20) NOT NULL PRIMARY KEY,
                           AGE                       INT(3) NOT NULL,
                           GENDER                    CHAR(10) NOT NULL,
                           MARITAL_STATUS            VARCHAR(30) NOT NULL,
                           CASTE                     VARCHAR(30),          
                           SUB_CASTE                 VARCHAR(30),    
                           STATE                     VARCHAR(30) NOT NULL,  
                           CITY                      VARCHAR(30) NOT NULL,  
                           COUNTRY                   VARCHAR(30) NOT NULL,  
                           HEIGHT                    FLOAT(6,2) NOT NULL,  
                           PHYSICAL_STATUS           VARCHAR(30) NOT NULL,  
                           FAMILY_STATUS             VARCHAR(30) NOT NULL,  
                           FAMILY_TYPE               VARCHAR(20) NOT NULL,  
                           FAMILY_VALUES             VARCHAR(20) NOT NULL,  
                           PARTNER_AGE               VARCHAR(15),
                           PARTNER_EDUCATION         VARCHAR(30),  
                           PARTNER_INCOME            VARCHAR(30) ,  
                           PARTNER_LOCATION          VARCHAR(30),  
                           ABOUT_DESCRIPTION         VARCHAR(300))"""  
                           
           cursor.execute(sql_member) 


      def insertVariblesIntoTable(self, PROFILE_ID, AGE, GENDER, MARITAL_STATUS, CASTE, SUB_CASTE,\
                                        STATE, CITY, COUNTRY, HEIGHT, PHYSICAL_STATUS, FAMILY_STATUS,\
                                        FAMILY_TYPE, FAMILY_VALUES, PARTNER_AGE, PARTNER_EDUCATION,\
                                        PARTNER_INCOME, PARTNER_LOCATION, ABOUT_DESCRIPTION):
                                        
           connection  =   self.connection                   
           try:
                cursor = connection.cursor()
               
                mySql_insert_query    = """INSERT INTO MEMBER (PROFILE_ID, AGE, GENDER, MARITAL_STATUS, CASTE, SUB_CASTE,
                                        STATE, CITY, COUNTRY, HEIGHT, PHYSICAL_STATUS, FAMILY_STATUS,
                                        FAMILY_TYPE, FAMILY_VALUES, PARTNER_AGE, PARTNER_EDUCATION,
                                        PARTNER_INCOME, PARTNER_LOCATION, ABOUT_DESCRIPTION)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s) """
        
                recordTuple = (PROFILE_ID, AGE, GENDER, MARITAL_STATUS, CASTE, SUB_CASTE,\
                                        STATE, CITY, COUNTRY, HEIGHT, PHYSICAL_STATUS, FAMILY_STATUS,\
                                        FAMILY_TYPE, FAMILY_VALUES, PARTNER_AGE, PARTNER_EDUCATION,\
                                        PARTNER_INCOME, PARTNER_LOCATION, ABOUT_DESCRIPTION)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into MEMBER table")
        
           except mysql.connector as error:
                print("Failed to insert into MySQL table %s " % error)
                
                        

###
### End of class
###