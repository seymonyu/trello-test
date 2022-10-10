from pytest_bdd import given, when, then
import requests
import json
import datetime
import pytest

key = '7a640808e3b65d0afa7a6247b54011e2'
token = 'fe6339bdbb1b8b97a19ce08b44e98094b7168d685c643f2015d19f24ba5c611e'
user_id = '5e216fe1aa6924614e068349'
url = "https://api.trello.com/"

headers = {
   "Accept": "application/json"
}

query = {
    'key': key,
    'token': token
}


@pytest.fixture
def step_context():
    return {'response': None}


@given("I am an authorized user")
def test_authorization():
    response = requests.request(
        "GET",
        url=f'{url}1/tokens/{token}/member',
        headers=headers,
        params=query
    )
    assert response.status_code == 200


@given("there is a board")
def test_check_board():
    response = requests.request(
        "GET",
        url=f'{url}1/members/{user_id}/boards',
        headers=headers,
        params=query
    )
    assert response.status_code == 200
    board_id = ""
    if response:
        board_id = response.json()[12]["id"]
        print(board_id)
        return board_id
    else:
        return board_id


@when("user creates a list")
def test_create_list():
    name_list = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
    query_list = {
        'name': name_list,
        'idBoard': '63446a765b4e5c00f5a24376',
        'key': key,
        'token': token
    }
    response = requests.request(
        "POST",
        url=f'{url}1/lists',
        params=query_list
    )
    pytest.response = response


@then("a list is created")
def test_check_created_list():
    print(pytest.response.text)
    assert pytest.response.status_code == 200

