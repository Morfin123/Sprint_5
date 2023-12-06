from selenium import webdriver
import locators
import time
from data_for_tests import TestAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorizations:

    def test_successful_authorization_on_button_personal_account(self):
        """
        Проверка успешной авторизации через кнопку "Личный кабинет"
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestAccount.user_password)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_LOGOUT)))
        assert driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'
        driver.quit()

    def test_successful_authorization_on_button_login_on_main_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти в аккаунт" на главной
            :return:
            """
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
            driver.get("https://stellarburgers.nomoreparties.site/")
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_MAIN_PAGE)))
            driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'
            driver.quit()

    def test_successful_authorization_on_button_login_on_registration_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти" на странице регистрации
            :return:
            """
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
            driver.get("https://stellarburgers.nomoreparties.site/register")
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_PAGE)))
            driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_REGISTRATION_PAGE).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'
            driver.quit()

    def test_successful_authorization_on_button_login_on_password_recovery_page(self):
            """
            Проверка успешной авторизации через кнопку "Войти" на странице восстановления пароля
            :return:
            """
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
            driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGIN_ON_PASS_RECOVERY_PAGE)))
            driver.find_element(By.XPATH, locators.BUTTON_LOGIN_ON_PASS_RECOVERY_PAGE).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL)))
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestAccount.user_email)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(
                TestAccount.user_password)
            driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
            time.sleep(1)
            driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUTTON_LOGOUT)))
            assert driver.find_element(By.XPATH, locators.BUTTON_LOGOUT).text == 'Выход'
            driver.quit()
