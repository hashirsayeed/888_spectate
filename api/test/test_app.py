import json
from api.app import app

#Test fucntion for SPORT using POST 
def test_success_sport_post():
    client = app.test_client()
    url = '/sport'

    mock_req_data = {
        "name": "Foot ball",
        "slug": "Foot ball",
        "active": 1
    }
    response = client.post(url, data=json.dumps(mock_req_data), content_type='application/json')
    print(response)
    assert response.status_code == 200

