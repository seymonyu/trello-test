from pytest_bdd import given, when, then


@given("has a card in a board")
def test_check_card():
    print('test')


@when("deletes the card")
def test_delete_card():
    print('test')


@then("the card is deleted")
def test_card_deleted():
    print('test')
