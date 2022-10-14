import os
from pytest_bdd import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


email = os.environ.get('TRELLO_EMAIL')
password = os.environ.get('TRELLO_PASSWORD')
url = "https://trello.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)


@given("A user is on the trello website")
def test_get_url():
    driver.get(url)


@when("the user clicks Log in")
def test_click_login():
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()


@given("the user enters a valid email <email> and password <password>")
def test_enter_credentials():
    driver.find_element(By.ID, 'user').send_keys(email)
    driver.find_element(By.ID, 'login').click()
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-submit').click()


@then("the should be successfully logged into the site")
def test_check_login():
    driver.find_element(By.CLASS_NAME, 'boards-page-board-section-header').is_displayed()


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