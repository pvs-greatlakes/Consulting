# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 07:58:40 2020

@author: PVS
"""

import random
from   datetime          import  datetime
import sys, os
import random
import string
import mysql.connector

folder_name = r'D:\Consulting\Matrimony'
sys.path.insert(0, folder_name) 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from db_Class_210821_matrimony  import  Member

error            =    None
mem              =    Member("localhost", "testUser", "A4min@123", "matrimony" )
connection       =    mem.db_connection()
mem.db_create_table()
        
### 
### Insert data 
###
                                           
PROFILE_ID            =   'M5929711'
AGE                   =   '27'
GENDER                =   'Female'
MARITAL_STATUS        =   'Never married'
CASTE                 =   'Mudaliar'
SUB_CASTE             =   'Melakarar'
STATE                 =   'Tamil Nadu'
CITY                  =   'Chennai' 
COUNTRY               =   'India' 
HEIGHT                =   '5.8' 
PHYSICAL_STATUS       =   'Normal' 
FAMILY_STATUS         =   'Middle Class'
FAMILY_TYPE           =   'Joint' 
FAMILY_VALUES         =   'Orthodox'  
PARTNER_AGE           =   '28-30' 
PARTNER_EDUCATION     =   'Graduate'
PARTNER_INCOME        =   '400000' 
PARTNER_LOCATION      =   'Tamil Nadu'                
ABOUT_DESCRIPTION     =   ''  

mem.insertVariblesIntoTable(PROFILE_ID, AGE, GENDER, MARITAL_STATUS, CASTE, SUB_CASTE,\
                                        STATE, CITY, COUNTRY, HEIGHT, PHYSICAL_STATUS, FAMILY_STATUS,\
                                        FAMILY_TYPE, FAMILY_VALUES, PARTNER_AGE, PARTNER_EDUCATION,\
                                        PARTNER_INCOME, PARTNER_LOCATION, ABOUT_DESCRIPTION) # 
            



### 


sql_select     =  """SELECT CONVERT(count(*), CHAR) FROM MEMBER"""
cursor         =  connection.cursor()
cursor.execute(sql_select)
count          =  cursor.fetchone()
        
print("\n Total MEMBER records inserted is %s" % count)



###