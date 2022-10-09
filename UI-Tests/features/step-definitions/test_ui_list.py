from pytest_bdd import scenario, given, when, then


@given("user is on a board")
def step_impl():
    raise NotImplementedError(u'STEP: Given user is on a board')


@when("user clicks 'Add another list'")
def step_impl():
    raise NotImplementedError(u'STEP: When user clicks \'Add another list\'')


@given("user enters 'testList' in the title")
def step_impl():
    raise NotImplementedError(u'STEP: And user enters \'testList\' in the title')


@then("a list with 'testList' title is created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a list with \'testList\' title is created')


@when("user creates a list")
def step_impl():
    raise NotImplementedError(u'STEP: When user creates a list')


@given("user leaves the title empty")
def step_impl():
    raise NotImplementedError(u'STEP: And user leaves the title empty')


@then("the list is not created")
def step_impl():
    raise NotImplementedError(u'STEP: Then the list is not created')


@given("a user is on a board with a list")
def step_impl():
    raise NotImplementedError(u'STEP: Given a user is on a board with a list')


@when("user clicks the list title")
def step_impl():
    raise NotImplementedError(u'STEP: When user clicks the list title')


@given("enters 'changeTitle'")
def step_impl():
    raise NotImplementedError(u'STEP: And enters \'changeTitle\'')


@then("the list name is changed to 'changeTitle'")
def step_impl():
    raise NotImplementedError(u'STEP: Then the list name is changed to \'changeTitle\'')


@when("the user clicks the three dots on the list")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks the three dots on the list')


@given("the user clicks 'archive this list'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks \'archive this list\'')


@then("the list is not displayed anymore")
def step_impl():
    raise NotImplementedError(u'STEP: Then the list is not displayed anymore')