import random
import pytest
import locators
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login():
    driver.find_element(BUTTON_LOGIN).click()