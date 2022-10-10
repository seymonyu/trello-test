
from selenium.webdriver.common.by import By


def login(driver, email, password):
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()
    driver.find_element(By.ID, 'user').send_keys(email)
    driver.find_element(By.ID, 'login').click()
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-submit').click()
    driver.find_element(By.CLASS_NAME, 'boards-page-board-section-header').is_displayed()
