import pytest
import time
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestConstructor:

    def test_transition_to_bread_rolls(self):
        """
        Проверка перехода к разделу "Булки"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        self.driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        self.driver.find_element(By.XPATH, locators.BUTTON_BREAD_ROLLS).click()
        time.sleep(1)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_BREAD_ROLLS)))
        assert self.driver.find_element(By.XPATH, locators.TITLE_BREAD_ROLLS).is_displayed()

    def test_transition_to_fillings(self):
        """
        Проверка перехода к разделу "Начинки"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        self.driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, locators.TITLE_FILLINGS).is_displayed()

    def test_transition_to_sauces(self):
        """
        Проверка перехода к разделу "Соусы"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        self.driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        self.driver.find_element(By.XPATH, locators.BUTTON_SAUCES).click()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, locators.TITLE_SAUCES).is_displayed()
