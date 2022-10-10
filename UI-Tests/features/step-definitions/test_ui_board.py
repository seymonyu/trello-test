from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


url = "https://trello.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@given("the user is on logged in on trello website")
def test_login():
    driver.implicitly_wait(10)  # seconds
    driver.get(url)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()
    driver.find_element(By.ID, 'user').send_keys('seymafirat@outlook.com')
    driver.find_element(By.ID, 'login').click()
    driver.find_element(By.ID, 'password').send_keys('qvuj83tva')
    driver.find_element(By.ID, 'login-submit').click()
    driver.find_element(By.CLASS_NAME, 'boards-page-board-section-header').is_displayed()


@when("the user clicks on 'Create'")
def test_click_create():
    driver.find_element(By.CLASS_NAME, 'YVxoA9yoN2HeNo').click()


@when("the user clicks on 'Create a board'")
def test_click_create_board():
    driver.find_element(By.CLASS_NAME, 'R2Zt2qKgQJtkYY').click()


@when("the user enters the title 'testBoard'")
def test_enter_board_name():
    driver.find_element(By.CLASS_NAME, 'nch-textfield__input').send_keys(
        'testBoard')
    driver.find_element(By.CLASS_NAME, 'G2lWjDVJsvar3H').click()


@then("a board is created")
def test_check_board():
    driver.find_element(By.CLASS_NAME, 'board-header-btn-text').is_displayed()
    board_name = driver.find_element(By.CLASS_NAME, 'board-header-btn-text').get_attribute("textContent")
    if board_name == 'testBoard':
        print('tests are passed!')