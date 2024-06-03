from flask import Flask, jsonify, request
from api.database import db_connection, insert_into_table_sport, update_in_table_sport, get_data_sport
from datetime import datetime
from app_helper.helper_class import Sport, Event, Selection

#creating application of flask
app = Flask(__name__)

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
        if req_data and len(req_data) > 0:
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
                name = ''
            
            if 'Active' in req_data:
                active = req_data['Active']
            else:
                missing = True
                error_msg += ' ,Avtive '
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
            id_after_update = update_in_table_sport(db, sport_id, name, slug, active)
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
@app.route('/sport', method = ['GET'])
def ret_data_sport():
    try:
        #createing a list to retrieve filtered data
        s_list = []
        #temp variable to get filters and converting the data into dictionary
        req_filters = request.args.to_dict()

        db = db_connection()
        filt_rows = get_data_sport(req_filters)
        if filt_rows:
            for r in filt_rows:
                s = {
                    'name': r['name'],
                    'slug': r['slug'],
                    'active': r['active']
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
        return jsonify({"message": "Something went wrong !"}, 400)
