from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import utils

url = "https://trello.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(20)  # seconds


@given("the user is on logged in on trello website")
def test_login():
    driver.get(url)
    utils.login(driver, os.environ.get('TRELLO_EMAIL'), os.environ.get('TRELLO_PASSWORD'))


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
    driver.implicitly_wait(20)
    driver.find_element(By.CLASS_NAME, 'board-header-btn').is_displayed()
    board_name = driver.find_element(By.CLASS_NAME, 'board-name-input').get_attribute("value")
    if board_name == 'testBoard':
        print('tests are passed!')

