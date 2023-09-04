import pymysql  
from config import HOST, USER, PASSWORD, DATABASE

db = pymysql.connect(
    host=HOST,    
    user=USER,  
    password=PASSWORD,  
    database=DATABASE  
)