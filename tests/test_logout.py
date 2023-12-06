from selenium import webdriver
import locators
import time
from data_for_tests import TestAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:

    def test_successful_logout_from_account(self):
        """
        Проверка успешного выхода из аккаунта через кнопку "Выйти" в Личном кабинете
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestAccount.user_password)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_LOGOUT)))
        driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN)))
        assert driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).text == 'Войти'
        driver.quit()
