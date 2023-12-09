import pytest
import time
import locators
from data_for_tests import TestAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestAuthorizations:

    def test_successful_authorization_on_button_personal_account(self):
        """
        Проверка успешной авторизации через кнопку "Личный кабинет"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestAccount.user_password)
        self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_LOGOUT)))
        assert self.driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'

    def test_successful_authorization_on_button_login_on_main_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти в аккаунт" на главной
            :return:
            """
            self.driver.get("https://stellarburgers.nomoreparties.site/")
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_MAIN_PAGE)))
            self.driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert self.driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'

    def test_successful_authorization_on_button_login_on_registration_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти" на странице регистрации
            :return:
            """
            self.driver.get("https://stellarburgers.nomoreparties.site/register")
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_AND_PASS_RECOVERY_PAGE)))
            self.driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_AND_PASS_RECOVERY_PAGE).click()
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert self.driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'

    def test_successful_authorization_on_button_login_on_password_recovery_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти" на странице восстановления пароля
            :return:
            """
            self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_AND_PASS_RECOVERY_PAGE)))
            self.driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_AND_PASS_RECOVERY_PAGE).click()
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            self.driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert self.driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'
