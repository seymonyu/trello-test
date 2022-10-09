from pytest_bdd import scenario, given, when, then


@given("A user is on the trello website")
def step_impl():
    raise NotImplementedError(u'STEP: Given A user is on the trello website')


@when("the user clicks Log in")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks Log in')


@given("the user enters a valid email <email> and password <password>")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters a valid email <email> and password <password>')


@then("the should be successfully logged into the site")
def step_impl():
    raise NotImplementedError(u'STEP: Then the should be successfully logged into the site')


@given("the user enters a valid email <email> and the wrong password <password>")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters a valid email <email> and the wrong password <password>')


@then("error message is shown indicating wrong email/password")
def step_impl():
    raise NotImplementedError(u'STEP: Then error message is shown indicating wrong email/password')


@given("the user enters invalid email <email>")
def step_impl():
    raise NotImplementedError(u'STEP: And the user enters invalid email <email>')


@then("the user is redirected to signup")
def step_impl():
    raise NotImplementedError(u'STEP: Then the user is redirected to signup')