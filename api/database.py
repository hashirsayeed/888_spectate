import mysql.connector
from api.logger import logger
import time
from helper import make_filter_sport

#function to create connecting to database
def db_connection():
    try:
        time.sleep(5)
        db = mysql.connector.connect(
            host = "localhost",
            user = 'root',
            passwd = 'Hashirs@10',
            database = 'test888database'
        )
        return db
    except Exception as e:
        mycursor = db.cursor()
        mycursor.close()
        print("Exception occurred while connecting to db:", e)

#function to insert values into sport table
def insert_into_table_sport(db, name, slug, active):
    try:
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO sport (id, name, slug, active) VALUE (%s, %s)", (name, slug, active))
        db.commit()
        return mycursor.lastrowid
    
    except Exception as e:
        mycursor.close()
        print("Exception occured while inserting into table sport: ", e)
        return None

#function to update the values in sport table
def update_in_table_sport(db, id, name, slug, active):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE sport SET name = %s, slug = %s, active = %s WHERE id = %s", (name, slug, active, id))
        db.commit()
        return id
    except Exception as e:
        mycursor.close()
        print("Exception occured while updating the record", e)
        return None

#function to retrive data with or without filters
def get_data_sport(db, filters):
    try:
        #query for selctions
        query = "SELECT * FROM sport"
        #filter query
        f_query = ""
        if filters:
            f_query = make_filter_sport(filters)
        query += f_query
        print(f"final query: {query}")
        mycursor = db.cursor()
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return rows
    except Exception as e:
        db.close()
        print("Error occured while retrieving sport", e)
        return None