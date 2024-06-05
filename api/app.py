from flask import Flask, jsonify, request
from api.database import db_connection, insert_into_table_sport, update_in_table_sport, get_data_sport, sport_deactivation, insert_into_event, get_data_event, event_deactivation, insert_into_selection, update_in_table_selection, get_data_selection, selection_deactivation
from datetime import datetime
from api.helper_class import Sport, Event, Selection

#creating application of flask
app = Flask(__name__)

######################################### SPORT ##############################################################
#function to create sports entity and updating entity in the table
#intitating methods for POST and PUT
@app.route('/sport', methods = ['POST', 'PUT'])
def create_update_sport():
    try:
        #get json data
        req_data = request.get_json()
        #creating an error message structure to differentiate if any fields are missing with a missing flag
        error_msg = "Field is missing"
        missing = False
        #check if data recieved is not null
        if req_data:
            #if the column is not in data change the flag otherwise take the value in a variable
            if 'Name' in req_data:
                name = req_data['Name']
            else:
                missing = True
                error_msg += ' ,Name '
                name = ''

            if 'Slug' in req_data:
                slug = req_data['Slug']
            else:
                missing = True
                error_msg += ' ,Slug '
                slug = ''
            
            if 'Active' in req_data:
                active = req_data['Active']
            else:
                missing = True
                error_msg += ' ,Active '
                active = ''
        else:
            #if there is no data to be saved in the table. Return a message with status 400
            return_message = {"message": "No data to save in the sport table!"}
            return jsonify(return_message), 400
        
        #if any field was missing return a message with status 400
        if missing:
            return_message = {"message": error_msg}
            return jsonify(return_message), 400
        
        sport = Sport(name, slug, active)
        db = db_connection()
        
        #if request is to add a new entry in the table using POST method
        if request.method == 'POST':
            last_id = insert_into_table_sport(db, sport.name, sport.slug, sport.active)
            print(f'Entry was created in sport table with id{last_id}')
            re_msg = {"message": 'Entry was created in sport table with id' + str(last_id)}
        elif request.method == 'PUT':
            #check if the id is there otherwise return the message
            if 'id' in req_data:
                sport_id = req_data['id']
            else:
                re_msg = {"message": "ID not provided!"}
                return jsonify(re_msg), 400
            sport.set_id(sport_id)
            id_after_update = update_in_table_sport(db, sport.id, name, slug, active)
            print(f"Entry was updated in the sport table with id {id_after_update}")
            re_msg = {"message": "Entry was updated with id" + str(id_after_update)}

        #if the task were successfull then close database connection and return message to status 200
        db.close()
        return jsonify(re_msg), 200
    
    except Exception as e:
        print('Error occured while doing operations in sport table', e)
        return jsonify({"message": "Something went wrong !"}), 400

#function to retrieve data from sport table
#initiating method for GET
@app.route('/sport', methods = ['GET'])
def ret_data_sport():
    try:
        #createing a list to retrieve filtered data
        s_list = []
        #temp variable to get filters and converting the data into dictionary
        req_filters = request.args.to_dict()

        db = db_connection()
        filt_rows = get_data_sport(db, req_filters)
        if filt_rows:
            for r in filt_rows:
                s = {
                    'name': r['Name'],
                    'slug': r['Slug'],
                    'active': r['Active']
                }
                s_list.append(s)
        #if all the data is retrieved clode database connection
        db.close()
        if s_list:
            return jsonify(s_list)
        else:
            return jsonify({"message": "No Sports AVAilable!"}), 200
    except Exception as e:
        print("Something went worng ret_data_sport funcitons: ", e)
        return jsonify({"message": "Something went wrong !"}), 400

#method to deactive a sport entry if all the events are inactive
@app.route('/sport_entry_deavtivation', methods = ['GET'])
def sport_entry_deavtivation():
    try:
        #converting the requested deactivation data into dictionary
        req_deact = request.args.to_dict()
        #if the given data is not empty and id is given for a sport entry
        #if data is empty of id is not provided. return the message with status 400
        if req_deact and 'id' in req_deact:
            id_sport = req_deact['id']
        else:
            return jsonify({"message": "No id was given for the sport entry! "}), 400
        db = db_connection()
        #when all queries are done successfully return status 200
        ret_id = sport_deactivation(db, id_sport)
        return jsonify({"message": "Sport entry deactivated!"}), 200

    except Exception as e:
        print("Something went worng in sport_entry_deactivation function!", e)
        return jsonify({"message": "Something went wrong!"}), 400


################################################# EVENT #########################################################
#function to create event entry and updating existing entries
#initiating method with POST and PUT
@app.route('/event', methods = ['POST', 'PUT'])
def create_update_event():
    try:
        #get json data
        req_data = request.get_json()
        #creating an error message structure to differentiate if any fields are missing with a missing flag
        error_msg = "Field is missing"
        missing = False
        #check if data recieved is not null
        if req_data:
            if 'Name' in req_data:
                name = req_data['Name']
            else:
                missing = True
                error_msg += ' ,Name '
                name = ''

            if 'Active' in req_data:
                active = req_data['Active']
            else:
                missing = True
                error_msg += ' ,Active '
                active = ''
            
            if 'Slug' in req_data:
                slug = req_data['Slug']
            else:
                missing = True
                error_msg += ' ,Slug '
                slug = ''
            
            if 'Type' in req_data:
                e_type = req_data['Type']
            else:
                missing = True
                error_msg += ' ,Type '
                e_type = ''
            
            if 'sport_id' in req_data:
                sport_id = req_data['sport_id']
            else:
                missing = True
                error_msg += ' ,Sport_ID '
                sport_id = ''

            if 'Status' in req_data:
                status = req_data['Status']
            else:
                missing = True
                error_msg += ' ,Status '
                status = ''
            
            if 'start_time' in req_data:
                st_time_temp = req_data['start_time']
                st_time = datetime.strptime(st_time_temp, '%Y-%m-%d %H:%M:%S')
            else:
                missing = True
                error_msg += ' ,start_time '
                st_time = ''
            
            if 'actual_start_time' in req_data:
                a_time_temp = req_data['actual_start_time']
                a_time = datetime.strptime(a_time_temp, '%Y-%m-%d %H:%M:%S')
            else:
                a_time = None
        else:
            return_message = {"message": "No data to save in the event table!"}
            return jsonify(return_message), 400
        
        #if any field was missing return a message with status 400
        if missing:
            return_message = {"message": error_msg}
            return jsonify(return_message), 400
        
        event = Event(name, active, slug, e_type, status, st_time, a_time, sport_id)
        db = db_connection()

        
        #if request is to add a new entry in the table using POST method
        if request.method == 'POST':
            sport_filter_id = {'sport_id': sport_id}
            sport = get_data_sport(db, sport_filter_id)
            print(sport)
            if not sport:
                return_message = {"message": "No active sport entry present for the ID given!"}
                return jsonify(return_message), 400
            
            last_id = insert_into_event(db, event.name, event.active, event.slug, event.type, event.status, event.start_time, event.actual_start_time, event.sport_id)
            print(f'Entry was created in event table with id{last_id}')
            re_msg = {"message": 'Entry was created in event table with id' + str(last_id)}
        elif request.method == 'PUT':
            #check if the id is there otherwise return the message
            if 'id' in req_data:
                event_id = req_data['id']
            else:
                re_msg = {"message": "ID not provided!"}
                return jsonify(re_msg), 400
            event.set_id(event_id)
            id_after_update = update_in_table_sport(db, name, active, slug, e_type, sport_id, status, st_time, a_time, event.id)
            print(f"Entry was updated in the event table with id {id_after_update}")
            re_msg = {"message": "Entry was updated with id" + str(id_after_update)}

        #if the task were successfull then close database connection and return message to status 200
        db.close()
        return jsonify(re_msg), 200
    except Exception as e:
        print('Error occured while doing operations in event table', e)
        return jsonify({"message": "Something went wrong !"}), 400

#function to retrieve data from event table
#initiating method for GET
@app.route('/event', methods = ['GET'])
def ret_data_event():
    try:
        #createing a list to retrieve filtered data
        e_list = []
        #temp variable to get filters and converting the data into dictionary
        req_filters = request.args.to_dict()

        db = db_connection()
        filt_rows = get_data_event(db, req_filters)
        if filt_rows:
            for r in filt_rows:
                e = {
                    'id': r['id'],
                    'name': r['Name'],
                    'slug': r['Slug'],
                    'active': r['Active'],
                    'type': r['Type'],
                    'sport_id': r['Sport_id'],
                    'status': r['Status'],
                    'start_time': r['start_time'],
                    'actual_start_time': r['actual_start_time']
                }
                e_list.append(e)
        #if all the data is retrieved clode database connection
        db.close()
        if e_list:
            return jsonify(e_list)
        else:
            return jsonify({"message": "No Events AVAilable!"}), 200
    except Exception as e:
        print("Something went worng ret_data_event funcitons: ", e)
        return jsonify({"message": "Something went wrong!"}), 400

#method to deactive a event entry if all the events are inactive
@app.route('/event_entry_deavtivation', methods = ['GET'])
def event_entry_deavtivation():
    try:
        #converting the requested deactivation data into dictionary
        req_deact = request.args.to_dict()
        #if the given data is not empty and id is given for a sport entry
        #if data is empty of id is not provided. return the message with status 400
        if req_deact and 'id' in req_deact:
            id_event = req_deact['id']
        else:
            return jsonify({"message": "No id was given for the event entry! "}), 400
        db = db_connection()
        #when all queries are done successfully return status 200
        ret_id = event_deactivation(db, id_event)
        return jsonify({"message": "Event entry deactivated!"}), 200

    except Exception as e:
        print("Something went worng in event_entry_deactivation function!", e)
        return jsonify({"message": "Something went wrong!"}), 400

################################################# SELECTION #########################################################
#function to create selection entry and updating existing entries
#initiating method with POST and PUT
@app.route('/selection', methods = ['POST', 'PUT'])
def create_update_selection():
    try:
        #get json data
        req_data = request.get_json()
        #creating an error message structure to differentiate if any fields are missing with a missing flag
        error_msg = "Field is missing"
        missing = False
        #check if data recieved is not null
        if req_data:
            if 'Name' in req_data:
                name = req_data['Name']
            else:
                missing = True
                error_msg += ' ,Name '
                name = ''

            if 'event_id' in req_data:
                event_id = req_data['event_id']
            else:
                missing = True
                error_msg += ' ,event_id '
                event_id = ''
            
            if 'Price' in req_data:
                price = req_data['Price']
            else:
                missing = True
                error_msg += ' ,Price '
                price = 0

            if 'Active' in req_data:
                active = req_data['Active']
            else:
                missing = True
                error_msg += ' ,Active '
                active = ''
            
            if 'Outcome' in req_data:
                outcome = req_data['Outcome']
            else:
                missing = True
                error_msg += ' ,Outcome '
                outcome = ''

        else:
            return_message = {"message": "No data to save in the selection table!"}
            return jsonify(return_message), 400
        
        #if any field was missing return a message with status 400
        if missing:
            return_message = {"message": error_msg}
            return jsonify(return_message), 400
        
        selection = Selection(name, event_id, price, active, outcome)
        db = db_connection()
        
        #if request is to add a new entry in the table using POST method
        if request.method == 'POST':
            event_filter_id = {'id': event_id}
            event = get_data_event(db, event_filter_id)
            if not event:
                return_message = {"message": "No active event entry was present for the ID given!"}
                return jsonify(return_message), 400
            
            last_id = insert_into_selection(db, selection.name, selection.event_id, selection.price, selection.active, selection.outcome)
            print(f'Entry was created in selection table with id{last_id}')
            re_msg = {"message": 'Entry was created in selection table with id' + str(last_id)}
        elif request.method == 'PUT':
            #check if the id is there otherwise return the message
            if 'id' in req_data:
                selection_id = req_data['id']
            else:
                re_msg = {"message": "ID not provided!"}
                return jsonify(re_msg), 400
            selection.set_id(selection_id)
            id_after_update = update_in_table_selection(db, name, event_id, price, active, outcome, selection.id)
            print(f"Entry was updated in the selection table with id {id_after_update}")
            re_msg = {"message": "Entry was updated with id" + str(id_after_update)}

        #if the task were successfull then close database connection and return message to status 200
        db.close()
        return jsonify(re_msg), 200
    except Exception as e:
        print('Error occured while doing operations in selection table', e)
        return jsonify({"message": "Something went wrong !"}), 400

#function to retrieve data from selection table
#initiating method for GET
@app.route('/selection', methods = ['GET'])
def ret_data_selection():
    try:
        #createing a list to retrieve filtered data
        s_list = []
        #temp variable to get filters and converting the data into dictionary
        req_filters = request.args.to_dict()

        db = db_connection()
        filt_rows = get_data_selection(db, req_filters)
        if filt_rows:
            for r in filt_rows:
                s = {
                    'id': r['id'],
                    'name': r['Name'],
                    'event_id': r['event_id'],
                    'price': r['Price'],
                    'active': r['Active'],
                    'outcome': r['Outcome']
                }
                s_list.append(s)
        #if all the data is retrieved clode database connection
        db.close()
        if s_list:
            return jsonify(s_list)
        else:
            return jsonify({"message": "No Selection Available!"}), 200
    except Exception as e:
        print("Something went worng ret_data_selection funcitons: ", e)
        return jsonify({"message": "Something went wrong!"}), 400

#method to deactive a selection entry if all the selections are inactive
@app.route('/selection_entry_deavtivation', methods = ['GET'])
def selection_entry_deavtivation():
    try:
        #converting the requested deactivation data into dictionary
        req_deact = request.args.to_dict()
        #if the given data is not empty and id is given for a sport entry
        #if data is empty of id is not provided. return the message with status 400
        if req_deact and 'id' in req_deact:
            id_selection = req_deact['id']
        else:
            return jsonify({"message": "No id was given for the event entry! "}), 400
        db = db_connection()
        #when all queries are done successfully return status 200
        ret_id = selection_deactivation(db, id_selection)
        return jsonify({"message": "Event entry deactivated!"}), 200

    except Exception as e:
        print("Something went worng in event_entry_deactivation function!", e)
        return jsonify({"message": "Something went wrong!"}), 400

if __name__ == "__main__":
    app.run(debug = True)
            
