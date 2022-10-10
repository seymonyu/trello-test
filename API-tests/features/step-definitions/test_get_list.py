from pytest_bdd import given, when, then
import requests
import pytest

key = '7a640808e3b65d0afa7a6247b54011e2'
token = 'fe6339bdbb1b8b97a19ce08b44e98094b7168d685c643f2015d19f24ba5c611e'
list_id = '63447c02b703e90017ba4714'
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


@given("there is a list on the board")
def test_check_board_for_lists():
    response = requests.request(
        "GET",
        url=f'{url}1/boards/{board_id}/lists',
        params=query
    )
    assert response.text is not None


@when("GET HTTP request is sent")
def test_get_list_with_id():
    response = requests.request(
        "GET",
        url=f'{url}1/lists/{list_id}',
        params=query
    )
    pytest.response = response


@then("the response is 200")
def test_check_response():
    assert pytest.response.status_code == 200