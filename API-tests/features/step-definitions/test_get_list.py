from pytest_bdd import given, when, then
import requests
import pytest
import config


headers = {
   "Accept": "application/json"
}

query = {
    'key': config.key,
    'token': config.token
}


@pytest.fixture
def step_context():
    return {'response': None}


@given("there is a list on the board")
def test_check_board_for_lists():
    response = requests.request(
        "GET",
        url=f'{config.url}1/boards/{config.board_id}/lists',
        params=query
    )
    assert response.text is not None


@when("GET HTTP request is sent")
def test_get_list_with_id():
    response = requests.request(
        "GET",
        url=f'{config.url}1/lists/{config.list_id}',
        params=query
    )
    pytest.response = response


@then("the response is 200")
def test_check_response():
    assert pytest.response.status_code == 200