import requests
import pytest

base_URL = 'https://restful-booker.herokuapp.com/booking'
auth_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200

@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token

@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "Narim",
        "lastname": "Mardanoff",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code == 200

def test_get_all_bookings():
    response = requests.get(base_URL)
    print(f'\n{len(response.json())}')
    assert response.status_code == 200
    key = 'Connection'
    assert key in response.headers
    print(f'\n{response.headers}')
    print(response.json())

def test_get_booking_with_ID():
    response = requests.get(f'{base_URL}/1')
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid']
    for key in expected_keys:
        assert key in response_data.keys()
    print(f'\n {response_data}')

def test_create_booking(booking_id):
    response = requests.get(f'{base_URL}/{booking_id}')
    assert response.status_code == 200
    assert response.json()['firstname'] == 'Eric'
def test_user_authorization():
    payload = {
    "username" : "admin",
    "password" : "password123"
}
    response = requests.post(auth_URL, json=payload)
    response_data = response.json()
    print(response.json())
    assert response.status_code == STATUS_OK
    assert 'token' in response_data

