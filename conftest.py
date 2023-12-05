import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

BUTTON_LOGIN = By.XPATH, "//button[text()=['Войти в аккаунт']"
INPUT_EMAIL = By.XPATH, "//*[@name='name']"
INPUT_PASSWORD = By.XPATH, "//*[type='Пароль']"

# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome()
#     driver.set_window_size(1920, 1080)
#     yield driver
#     driver.quit()

@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((INPUT_EMAIL)))
    yield driver
    driver.quit()