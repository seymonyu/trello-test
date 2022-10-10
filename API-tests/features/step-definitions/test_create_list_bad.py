from pytest_bdd import given, when, then
import requests
import pytest

key = '7a640808e3b65d0afa7a6247b54011e2'
token = 'fe6339bdbb1b8b97a19ce08b44e98094b7168d685c643f2015d19f24ba5c611e'
user_id = '5e216fe1aa6924614e068349'
board_id = '63446a765b4e5c00f5a24376'
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


@given("there is a board")
def test_check_board():
    response = requests.request(
        "GET",
        url=f'{url}1/members/{user_id}/boards/{board_id}',
        headers=headers,
        params=query
    )
    assert response.status_code == 200


@when("user creates a list without title")
def test_create_list_without_title():
    query_list = {
        'idBoard': board_id,
        'key': key,
        'token': token
    }
    response = requests.request(
        "POST",
        url=f'{url}1/lists',
        params=query_list
    )
    pytest.response = response


@then("the response is 400")
def test_status_check():
    assert pytest.response.status_code == 400
