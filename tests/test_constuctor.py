from selenium import webdriver
import locators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_transition_to_bread_rolls(self):
        """
        Проверка перехода к разделу "Булки"
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        driver.find_element(By.XPATH, locators.BUTTON_BREAD_ROLLS).click()
        time.sleep(1)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_BREAD_ROLLS)))
        assert driver.find_element(By.XPATH, locators.TITLE_BREAD_ROLLS).is_displayed()

    def test_transition_to_fillings(self):
        """
        Проверка перехода к разделу "Начинки"
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, locators.TITLE_FILLINGS).is_displayed()

    def test_transition_to_sauces(self):
        """
        Проверка перехода к разделу "Соусы"
        :return:
        """
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
        time.sleep(1)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TITLE_FILLINGS)))
        driver.find_element(By.XPATH, locators.BUTTON_SAUCES).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, locators.TITLE_SAUCES).is_displayed()
