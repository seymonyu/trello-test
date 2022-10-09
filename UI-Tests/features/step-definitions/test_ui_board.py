from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://trello.com/"

service = Service(executable_path="Users/seymafirat/Applications/chromedriver")
driver = webdriver.Chrome(service=service)


@given("the user is on logged in on trello website")
def test_login():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")


@when("the user clicks on 'Create'")
def step_impl():
    raise NotImplementedError(u'STEP: When the user clicks on \'Create\'')
