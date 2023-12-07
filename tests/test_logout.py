import pytest
import time
import locators
from data_for_tests import TestAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestLogout:

    def test_successful_logout_from_account(self):
        """
        Проверка успешного выхода из аккаунта через кнопку "Выйти" в Личном кабинете
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestAccount.user_password)
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_LOGOUT)))
        self.driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN)))
        assert self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).text == 'Войти'
