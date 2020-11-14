import mysql.connector
from mysql.connector import Error
#from django.test import TestCase

# Create your tests here.


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='stadium',
                                         user='root',
                                         password='qwertyuiop@12')
    if connection.is_connected():
        cursor = connection.cursor()
        
except Error as e:
    print("Error while connecting to MySQL", e)