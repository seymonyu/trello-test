from pytest_bdd import scenario, given, when, then


@given("the user is on logged in on trello website")
def step_impl():
    raise NotImplementedError(u'STEP: Given the user is on logged in on trello website')


@when("the user clicks on 'Create'")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks on \'Create\'')


@given("the user clicks on 'Create a board'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks on \'Create a board\'')


@given("the user enters the title 'testBoard'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters the title \'testBoard\'')


@then("a board is created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a board is created')


@given("the user is on trello website")
def step_impl():
    raise NotImplementedError(u'STEP: Given the user is on trello website')


@then("the Create board button is not available")
def step_impl():
    raise NotImplementedError(u'STEP: Then the Create board button is not available')


@when("the user clicks on 'testBoard'")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks on \'testBoard\'')


@then("the board with title 'testBoard' is displayed")
def step_impl():
    raise NotImplementedError(u'STEP: Then the board with title \'testBoard\' is displayed')


@given('the user is on board "RxAUsjbL"')
def step_impl():
    raise NotImplementedError(u'STEP: And the user is on board "RxAUsjbL"')


@when("the user clicks the board title")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks the board title')


@given("the user enters 'updateTitle'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters \'updateTitle\'')


@then("the board title is updated to 'updateTitle'")
def step_impl():
    raise NotImplementedError(u'STEP: Then the board title is updated to \'updateTitle\'')


@when("the user clicks the three dots on the right of the screen")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks the three dots on the right of the screen')


@given("the user clicks more")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks more')


@given("the user clicks close board")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks close board')


@then("the board is closed")
def step_impl():
    raise NotImplementedError(u'STEP: Then the board is closed')


@given("the user just closed a board")
def step_impl():
    raise NotImplementedError(u'STEP: Given the user just closed a board')


@when("the user clicks 'Permanently delete board'")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks \'Permanently delete board\'')


@given("the user clicks 'Delete' on the popup")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks \'Delete\' on the popup')


@then("the board is deleted")
def step_impl():
    raise NotImplementedError(u'STEP: Then the board is deleted')


@given("the user is taken to the main screen")
def step_impl():
    raise NotImplementedError(u'STEP: And the user is taken to the main screen')