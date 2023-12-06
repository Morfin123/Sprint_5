from selenium import webdriver
import locators
from data_for_tests import TestRandomAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_successful_registration(self):
        """
        Проверка успешной регистрации
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_START_REGISTRATION)))
        driver.find_element(By.XPATH, locators.BUTTON_START_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_DO_REGISTRATION)))
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_NAME).send_keys(TestRandomAccount.user_name)
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_EMAIL).send_keys(TestRandomAccount.user_email)
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_PASSWORD).send_keys(TestRandomAccount.password)
        driver.find_element(By.XPATH, locators.BUTTON_DO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_START_REGISTRATION)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_bad_password_on_registration(self):
        """
        Проверка ошибки ввода пароля при регистрации
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.BUTTON_DO_REGISTRATION)))
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_NAME).send_keys(TestRandomAccount.user_name)
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_EMAIL).send_keys(TestRandomAccount.user_email)
        driver.find_element(By.XPATH, locators.REGISTRATION_INPUT_PASSWORD).send_keys(TestRandomAccount.bad_password)
        driver.find_element(By.XPATH, locators.BUTTON_DO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.ERROR_PASSWORD)))
        assert driver.find_element(By.XPATH, locators.ERROR_PASSWORD).text == 'Некорректный пароль'
        driver.quit()
