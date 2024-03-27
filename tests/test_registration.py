import pytest
import locators
from data_for_tests import TestRandomAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestRegistration:

    def test_successful_registration(self):
        """
        Проверка успешной регистрации
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.PERSONAL_ACCOUNT))).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.BUTTON_START_REGISTRATION))).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.REGISTRATION_INPUT_NAME))).send_keys(TestRandomAccount.user_name)
        self.driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_EMAIL).send_keys(TestRandomAccount.user_email)
        self.driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_PASSWORD).send_keys(TestRandomAccount.password)
        self.driver.find_element(By.XPATH, locators.BUTTON_DO_REGISTRATION).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_START_REGISTRATION)))
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_bad_password_on_registration(self):
        """
        Проверка ошибки ввода пароля при регистрации
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.REGISTRATION_INPUT_NAME))).send_keys(TestRandomAccount.user_name)
        self.driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_EMAIL).send_keys(TestRandomAccount.user_email)
        self.driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_PASSWORD).send_keys(
            TestRandomAccount.bad_password)
        self.driver.find_element(By.XPATH, locators.BUTTON_DO_REGISTRATION).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.ERROR_PASSWORD)))
        assert self.driver.find_element(By.XPATH, locators.ERROR_PASSWORD).text == 'Некорректный пароль'
