from pytest_bdd import given, when, then
import requests


url = "https://api.trello.com/1/cards/{id}/idLabels"

query = {
   'key': 'APIKey',
   'token': 'APIToken'
}

response = requests.request(
   "POST",
   url,
   params=query
)


@given("the user is on a board with at least one list")
def test_one():
    print(response.text)


@when("a card is created")
def step_impl():
    raise NotImplementedError(u'STEP: When a card is created')


@then("the card is shown on the list")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is shown on the list')


@given("there are no lists on the board")
def step_impl():
    raise NotImplementedError(u'STEP: Given there are no lists on the board')


@then("an error is shown")
def step_impl():
    raise NotImplementedError(u'STEP: Then an error is shown')


@given("the trello website is opened")
def step_impl():
    raise NotImplementedError(u'STEP: Given the trello website is opened')


@when("the user is not logged in")
def step_impl():
    raise NotImplementedError(u'STEP: When the user is not logged in')


@then("the user cannot create a card")
def step_impl():
    raise NotImplementedError(u'STEP: Then the user cannot create a card')


@when("the user selects a card")
def step_impl():
    raise NotImplementedError(u'STEP: When the user selects a card')


@given("the edits the card title to 'test edit'")
def step_impl():
    raise NotImplementedError(u'STEP: And the edits the card title to \'test edit\'')


@then("the card title is updated")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card title is updated')


@given("the user adds a label")
def step_impl():
    raise NotImplementedError(u'STEP: And the user adds a label')


@then("the card is updated with the label")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is updated with the label')


@when("the user clicks the pencil icon on the card")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks the pencil icon on the card')


@given("clicks 'Open card'")
def step_impl():
    raise NotImplementedError(u'STEP: And clicks \'Open card\'')


@then("the card is displayed")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is displayed')


@given("user is opened a card")
def step_impl():
    raise NotImplementedError(u'STEP: Given user is opened a card')


@when("the user clicks 'Archive card' button")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks \'Archive card\' button')


@given("the user clicked 'Delete' button")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicked \'Delete\' button')


@then("the card is deleted")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is deleted')


@given("clicks 'Archive'")
def step_impl():
    raise NotImplementedError(u'STEP: And clicks \'Archive\'')


@then("the card is archived")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is archived')