from pytest_bdd import given, when, then
import requests
import datetime
import pytest
import config


@pytest.fixture
def step_context():
    return {'response': None}


@given("I am an authorized user")
def test_authorization():
    response = requests.request(
        "GET",
        url=f'{config.url}1/tokens/{config.token}/member',
        headers=config.headers,
        params=config.query
    )
    assert response.status_code == 200


@given("there is a board")
def test_check_board():
    response = requests.request(
        "GET",
        url=f'{config.url}1/members/{config.user_id}/boards',
        headers=config.headers,
        params=config.query
    )
    assert response.status_code == 200
    board_id = ""
    if response:
        board_id = response.json()[2]["id"]
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
        'key': config.key,
        'token': config.token
    }
    response = requests.request(
        "POST",
        url=f'{config.url}1/lists',
        params=query_list
    )
    pytest.response = response


@then("a list is created")
def test_check_created_list():
    print(pytest.response.text)
    assert pytest.response.status_code == 200


