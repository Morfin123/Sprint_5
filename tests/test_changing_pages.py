import pytest
import time
import locators
from data_for_tests import TestAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestChangingPages:

    def test_go_to_personal_account(self):
        """
        Провера перехода в личный кабинет по кнопке "Личный кабинет"
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
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        assert self.driver.find_element(By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT).text == \
               'В этом разделе вы можете изменить свои персональные данные'

    def test_go_to_constructor_from_personal_account(self):
        """
        Провера перехода в конструктор из личной учетной записи по кнопке "Конструктор"
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
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        self.driver.find_element(By.XPATH, locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert self.driver.find_element(By.XPATH, locators.CONSTRUCTOR_HEADER).text == 'Соберите бургер'

    def test_go_to_main_page_from_personal_account(self):
        """
        Провера перехода на главную из личной учетной записи по кнопке "Логотипа"
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
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        self.driver.find_element(By.CLASS_NAME, locators.LOGO).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert self.driver.find_element(By.XPATH, locators.CONSTRUCTOR_HEADER).text == 'Соберите бургер'
