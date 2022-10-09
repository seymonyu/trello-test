from pytest_bdd import scenario, given, when, then


@given("the user is on a board with at least one list")
def step_impl():
    raise NotImplementedError(u'STEP: Given the user is on a board with at least one list')


@when("the user clicks 'Add card'")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks \'Add card\'')


@given("the user enters 'myCard'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters \'myCard\'')


@then("the card is created")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is created')


@when("the user selects a card")
def step_impl():
    raise NotImplementedError(u'STEP: When the user selects a card')


@given("the edits the card title to 'editCard'")
def step_impl():
    raise NotImplementedError(u'STEP: And the edits the card title to \'editCard\'')


@then("the card title is updated")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card title is updated')


@given("the user clicks the 'Labels'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks the \'Labels\'')


@given("the user selects the first label")
def step_impl():
    raise NotImplementedError(u'STEP: And the user selects the first label')


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


@given("clicks 'Archive'")
def step_impl():
    raise NotImplementedError(u'STEP: And clicks \'Archive\'')


@then("the card is archived")
def step_impl():
    raise NotImplementedError(u'STEP: Then the card is archived')


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