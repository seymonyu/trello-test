from pytest_bdd import given, when, then
import requests
import pytest
import config


@pytest.fixture
def step_context():
    return {'response': None}


@given("there is a board")
def test_check_board():
    response = requests.request(
        "GET",
        url=f'{config.url}1/members/{config.user_id}/boards',
        headers=config.headers,
        params=config.query
    )
    assert response.status_code == 200


@when("user creates a list without title")
def test_create_list_without_title():

    response = requests.request(
        "POST",
        url=f'{config.url}1/lists',
        params=config.query_list
    )
    pytest.response = response


@then("the response is 400")
def test_status_check():
    assert pytest.response.status_code == 400
