from pytest_bdd import scenario, given, when, then


@given("user is on a board")
def step_impl():
    raise NotImplementedError(u'STEP: Given user is on a board')


@when("user creates a list")
def step_impl():
    raise NotImplementedError(u'STEP: When user creates a list')


@given("user enters 'test' in the title")
def step_impl():
    raise NotImplementedError(u'STEP: And user enters \'test\' in the title')


@then("a list is created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a list is created')


@given("user leaves the title empty")
def step_impl():
    raise NotImplementedError(u'STEP: And user leaves the title empty')


@then("an error message is shown")
def step_impl():
    raise NotImplementedError(u'STEP: Then an error message is shown')


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


@given("enters ''")
def step_impl():
    raise NotImplementedError(u'STEP: And enters \'\'')


@then("the list name is not changed")
def step_impl():
    raise NotImplementedError(u'STEP: Then the list name is not changed')


@when("the user clicks the three dots on the list")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks the three dots on the list')


@given("the user clicks 'archive this list'")
def step_impl():
    raise NotImplementedError(u'STEP: And the user clicks \'archive this list\'')


@then("the list is not displayed anymore")
def step_impl():
    raise NotImplementedError(u'STEP: Then the list is not displayed anymore')