import pytest
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("get_driver")
class TestConstructor:
    class_attribute_selected_section = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_transition_to_bread_rolls(self):
        """
        Проверка перехода к разделу "Булки"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.BUTTON_FILLINGS))).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        self.driver.find_element(By.XPATH, locators.BUTTON_BREAD_ROLLS).click()
        assert self.driver.find_element(By.XPATH, locators.TITLE_BREAD_ROLLS).is_displayed() and \
               self.driver.find_element(By.XPATH, locators.BUTTON_BREAD_ROLLS).get_attribute("class") \
               == TestConstructor.class_attribute_selected_section

    def test_transition_to_fillings(self):
        """
        Проверка перехода к разделу "Начинки"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.BUTTON_FILLINGS))).click()
        assert self.driver.find_element(By.XPATH, locators.TITLE_FILLINGS).is_displayed() and \
               self.driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).get_attribute("class") \
               == TestConstructor.class_attribute_selected_section

    def test_transition_to_sauces(self):
        """
        Проверка перехода к разделу "Соусы"
        :return:
        """
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.BUTTON_FILLINGS))).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        self.driver.find_element(By.XPATH, locators.BUTTON_SAUCES).click()
        assert self.driver.find_element(By.XPATH, locators.TITLE_SAUCES).is_displayed() and \
               self.driver.find_element(By.XPATH, locators.BUTTON_SAUCES).get_attribute("class") \
               == TestConstructor.class_attribute_selected_section
