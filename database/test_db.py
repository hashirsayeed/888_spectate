import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = 'Hashirs@10',
    database = 'test888database'
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE test888database")

#create a tables
def create_tables(mycursor):
    mycursor.execute("CREATE TABLE sport (Name VARCHAR(50), Slug VARCHAR(128) NULL, Active bool, ID int PRIMARY KEY AUTO_INCREMENT)")