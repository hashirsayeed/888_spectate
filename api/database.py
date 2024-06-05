import mysql.connector
from api.logger import logger
import time
from helper import make_filter_sport, make_filter_event, make_filter_selection  

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
        mycursor.execute("INSERT INTO sport (id, name, slug, active) VALUE (%s, %s, %s)", (name, slug, active))
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
        mycursor.execute("UPDATE sport SET Name = %s, Slug = %s, Active = %s WHERE id = %s", (name, slug, active, id))
        db.commit()
        return id
    except Exception as e:
        mycursor.close()
        print("Exception occured while updating the record in sport table", e)
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

#function to deactive a sport entry
def sport_deactivation(db, sport_id):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE sport SET active = 0 WHERE id = %s", str(sport_id))
        db.commit()
        return sport_id
    except Exception as e:
        db.close()
        print("Error occured while deactivating sport entry!", e)
        return None

#function to insert into event table
def insert_into_event(db, name, active, slug, e_type, sport_id, status, st_time, a_time):
    try:
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO event (id, Name, Active, Slug, Type, sport_id, Status, start_time, actual_star_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, active, slug, e_type, sport_id, status, st_time, a_time))
        db.commit()
        return mycursor.lastrowid
    except Exception as e:
        mycursor.close()
        print("Exception occured while inserting into table event: ", e)
        return None

#function to update the values in event table
def update_in_table_event(db, name, active, slug, e_type, sport_id, status, st_time, a_time, id):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE event SET Name = %s, Active = %s, Slug = %s, Type = %s, Sport_id = %s, Status = %s, start_time = %s, actual_start_time = %s WHERE id = %s", (name, active, slug, e_type, sport_id, status, st_time, a_time, id))
        db.commit()
        return id
    except Exception as e:
        mycursor.close()
        print("Exception occured while updating the record in event table", e)
        return None

#function to retrive data with or without filters
def get_data_event(db, filters):
    try:
        #query for selctions
        query = "SELECT * FROM event"
        #filter query
        f_query = ""
        if filters:
            f_query = make_filter_event(filters)
        query += f_query
        print(f"final query: {query}")
        mycursor = db.cursor()
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return rows
    except Exception as e:
        db.close()
        print("Error occured while retrieving event", e)
        return None

#function to deactive a event entry
def event_deactivation(db, event_id):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE event SET active = 0 WHERE id = %s", str(event_id))
        db.commit()
        return event_id
    except Exception as e:
        db.close()
        print("Error occured while deactivating event entry!", e)
        return None

#function to insert a new selection entry
def insert_into_selection(db, name, event_id, price, active, outcome):
    try:
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO selection (id, Name, event_id, Price, Active, Outcome) VALUES (%s, %s, %s, %s, %s)", (name, event_id, price, active, outcome))
        db.commit()
        return mycursor.lastrowid
    except Exception as e:
        mycursor.close()
        print("Exception occured while inserting into table selection: ", e)
        return None

#function to update the values in event table
def update_in_table_selection(db, name, event_id, price, active, outcome, id):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE selection SET Name = %s, event_id = %s, Price = %s, Active = %s, Outcome = %s WHERE id = %s", (name, event_id, price, active, outcome, id))
        db.commit()
        return id
    except Exception as e:
        mycursor.close()
        print("Exception occured while updating the record in selection table", e)
        return None

#function to retrive data with or without filters
def get_data_selection(db, filters):
    try:
        #query for selections
        query = "SELECT * FROM selection"
        #filter query
        f_query = ""
        if filters:
            f_query = make_filter_selection(filters)
        query += f_query
        print(f"final query: {query}")
        mycursor = db.cursor()
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return rows
    except Exception as e:
        db.close()
        print("Error occured while retrieving selections", e)
        return None

#function to deactive a selection entry
def selection_deactivation(db, selection_id):
    try:
        mycursor = db.cursor()
        mycursor.execute("UPDATE selection SET active = 0 WHERE id = %s", str(selection_id))
        db.commit()
        return selection_id
    except Exception as e:
        db.close()
        print("Error occured while deactivating selection entry!", e)
        return None