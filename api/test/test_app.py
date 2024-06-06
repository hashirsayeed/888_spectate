import json
from api.app import app

#Testing fucntion for SPORT table using POST with active as 1  
def test_success_sport_post():
    client = app.test_client()
    url = '/sport'

    mock_req_data = {
        "Name": "Foot ball",
        "Slug": "Foot ball",
        "Active": 1
    }
    response = client.post(url, data=json.dumps(mock_req_data), content_type='application/json')
    assert response.status_code == 200

#Testing function failure for SPORT table with missing field
def test_fail_sport_post():
    client = app.test_client()
    url = '/sport'
    mock_req_data = {}
    response = client.post(url, data=json.dumps(mock_req_data), content_type='application/json')
    assert response.status_code == 400

#Testing failure with missing name field
def test_fail_sport_m_name():
    client = app.test_client()
    url = '/sport'
    mock_req_data = {
        "Slug": "Football",
        "Active": 1
    }
    response = client.post(url, data=json.dumps(mock_req_data), content_type='application/json')
    assert response.status_code == 400

#Tesing failure with missing slug field
def test_fail_sport_m_slug():
    client = app.test_client()
    url = '/sport'
    mock_req_data = {
        "Name": "Football",
        "Active": 1
    }
    response = client.post(url, data=json.dumps(mock_req_data), content_type='application/json')
    assert response.status_code == 400

#Testing updating of field in sport table using put
def test_success_sport_put():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {
        "id": 1,
        "Name": "Football ball",
        "Slug": "Football ball",
        "Active": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 200

#Testing updating of field in sport table without giving ID
def test_fail_sport_put():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {
        "Name": "Football ball",
        "Slug": "Football ball",
        "Active": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400

#Testing updating sport table without any data
def test_fail_sport_m_data():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {}

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400

#Testing updating sport table with missing name
def test_fail_sport_m_name():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {
        "id": 1,
        "Slug": "Football ball",
        "Active": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400

#Testing updating sport table with missing slug
def test_fail_sport_m_slug():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {
        "id": 1,
        "Name": "Football ball",
        "Active": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400

#Testing updating sport table with missing active
def test_fail_sport_m_slug():
    client = app.test_client()
    url = '/sport'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Slug": "Football"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    assert response.status_code == 400

#Testing retreiving values from sport table with GET method
def test_success_sport_get():
    client = app.test_client()
    url = '/sport'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


#Testing retrieving values from sport table with an ID
def test_success_sport_get_id():
    client = app.test_client()
    url = '/sport?id=1'
    response = client.get(url)
    assert response.status_code == 200

#Testing retreiving values from sport table when an ID is not present
def test_success_sport_get_not_id():
    client = app.test_client()
    url = '/sport?id=70'
    response = client.get(url)
    assert response.status_code == 200

# #Testing retreiving all values from sport table with name
def test_success_sport_get_name():
    client = app.test_client()
    url = '/sport?name=Football'
    response = client.get(url)
    assert response.status_code == 200

# #Testing retreiving values from sport table with an ID and name
def test_success_sport_get_not_id():
    client = app.test_client()
    url = '/sport?id=1&name=Football'
    response = client.get(url)
    assert response.status_code == 200

# #Testing deactivating an entry in sport table
def test_success_sport_deactivate():
    client = app.test_client()
    url = '/sport_entry_deavtivation?id=1'
    response = client.get(url)
    assert response.status_code == 200

# #Testing fail of function deactivate_sport in sport table
def test_fail_sport_deactivate():
    client = app.test_client()
    url = '/sport_entry_deavtivation'
    response = client.get(url)
    assert response.status_code == 400

#Testing for event table 
#Testing for adding entry to the table
def test_success_event_post():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "sport_id": 1
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 200

#Testing inserting data into event table with no data
def test_fail_event_post_m_data():
    client = app.test_client()
    url = '/event'
    mock_request_data = {}
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing inserting data into event table with no name
def test_fail_event_post_m_name():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "sport_id": 1
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing inserting data into event table with no slug
def test_fail_event_post_m_slug():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "sport_id": 1
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing inserting data into event table with wrong type
def test_fail_event_post_w_type():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "WrongIP",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "sport_id": 1
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing inserting data into event table with no sport ID
def test_fail_event_post_m_sport_ID():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00"
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing inserting data into event table with wrong status
def test_fail_event_post_w_status():
    client = app.test_client()
    url = '/event'
    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "WrongST",
        "start_time": "2022-08-21 16:30:00",
        "sport_id": 1
    }
    response = client.post(url, data=json.dumps(mock_request_data), content_type = 'application/json')
    print(response)
    assert response.status_code == 400

#Testing for updating an entry in event table
def test_put_event_success():
    client = app.test_client()
    url = '/event'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "actual_start_time": "2022-08-21 16:30:00",
        "sport_id": 6
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200

#Testing for failrure updating an entry in event table with no id
def test_put_events_fail():
    client = app.test_client()
    url = '/event'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Slug": "Football",
        "Type": "Inplay",
        "Status": "Pending",
        "start_time": "2022-08-21 16:30:00",
        "actual_start_time": "2022-08-21 16:30:00",
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing for retrieving data from event
def test_success_event_get():
    client = app.test_client()
    url = '/event'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for retreiving data using ID
def test_get_events_success_id():
    client = app.test_client()
    url = '/event?id=1'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for retreiving data when ID is not present
def test_get_events_success_m_id():
    client = app.test_client()
    url = '/event?id=99'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for retreiving data using name
def test_get_events_success_name():
    client = app.test_client()
    url = '/event?Name=Football'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for retrieving data using name and ID
def test_get_events_success_name_id():
    client = app.test_client()
    url = '/event?id=1&Name=Football'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for deactivating entry in event table
def test_success_evnt_deactive():
    client = app.test_client()
    url = '/event_entry_deavtivation?id=1'
    response = client.get(url)
    print(response)
    assert response.status_code == 200
    

#Testing for deactivating entry in event table failure
def test_fail_evnt_deactive():
    client = app.test_client()
    url = '/event_entry_deavtivation'
    response = client.get(url)
    print(response)
    assert response.status_code == 400

#Testing for adding entry to selection table using PUT method
def test_success_selection_put():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Price": "2.00",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200

#Testing failure for adding entry to selection table with no data
def test_fail_selection_put_m_data():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing name
def test_fail_selection_put_m_name():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Price": "2.00",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing Price
def test_fail_selection_put_m_price():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing Active
def test_fail_selection_put_m_active():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with Wrong Active
def test_fail_selection_put_wrong_active():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 4,
        "Price": "2.0",
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing Price
def test_fail_selection_put_m_price():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing Outcome
def test_fail_selection_put_m_outcome():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Price": "2.0",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with Wrong Outcome
def test_fail_selection_put_w_outcome():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Price": "2.0",
        "Outcome": "WrongOC",
        "event_id": 1
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with missing event ID
def test_fail_selection_put_m_event_ID():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Price": "2.0",
        "Outcome": "Unsettled"
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing failure for adding entry to selection table with wrong event ID
def test_fail_selection_put_w_event_ID():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "Name": "Football",
        "Active": 1,
        "Price": "2.0",
        "Outcome": "Unsettled",
        "event_id": 99
    }

    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection
def test_seccess_selection_put():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Price": "2.00",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 200

#Testing to update an entry in selection with missing name
def test_seccess_selection_put_m_name():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Price": "2.00",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection with missing event_id
def test_seccess_selection_put_m_eventID():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Price": "2.00",
        "Active": 1,
        "Outcome": "Unsettled"
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection with missing price
def test_seccess_selection_put_m_price():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Active": 1,
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection with wring active
def test_seccess_selection_put_w_active():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Price": "2.00",
        "Active": "FALSE",
        "Outcome": "Unsettled",
        "event_id": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection with wring outcome
def test_seccess_selection_put_w_outcome():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Price": "2.00",
        "Active": 1,
        "Outcome": "WrongOC",
        "event_id": 1
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to update an entry in selection with wrong event_id
def test_seccess_selection_put_w_eventID():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {
        "id": 1,
        "Name": "Football",
        "Price": "2.00",
        "Active": "FALSE",
        "Outcome": "Unsettled",
        "event_id": 99
    }

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400


#Testing to update an entry in selection with no data
def test_fail_selection_put_m_id_m_data():
    client = app.test_client()
    url = '/selection'

    mock_request_data = {}

    response = client.put(url, data=json.dumps(mock_request_data), content_type='application/json')
    print(response)
    assert response.status_code == 400

#Testing to retrieve entries from selection table
def test_success_selection_get():
    client = app.test_client()
    url = '/selection'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing to retrieve entries from selection table using ID
def test_success_selection_get_ID():
    client = app.test_client()
    url = '/selection?id=1'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing to retrieve entries from selection table with ID not present in table
def test_success_selection_get_n_ID():
    client = app.test_client()
    url = '/selection?id=99'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing to retrieve entries from selection table using name
def test_success_selection_get_name():
    client = app.test_client()
    url = '/selection?Name=Football'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


#Testing to retrieve entries from selection table using name and ID
def test_success_selection_get_name_ID():
    client = app.test_client()
    url = '/selection?Name=Football&id=1'
    response = client.get(url)
    print(response)
    assert response.status_code == 200

#Testing for deactivation an entry in selection table
def test_success_deactivate_selection():
    client = app.test_client()
    url = '/selection_entry_deavtivation?id=1'
    response = client.get(url)
    print(response)
    assert response.status_code == 200


#Testing for fail of deactivation an entry in selection table
def test_fail_deactivate_selection():
    client = app.test_client()
    url = '/selection_entry_deavtivation'
    response = client.get(url)
    print(response)
    assert response.status_code == 400







