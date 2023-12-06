from selenium import webdriver
import locators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestChangingPages:
    user_email = f"test123@test.test"
    user_password = f"test123456"

    def test_go_to_personal_account(self):
        """
        Провера перехода в личный кабинет по кнопке "Личный кабинет"
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
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestChangingPages.user_email)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestChangingPages.user_password)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        assert driver.find_element(By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT).text == \
               'В этом разделе вы можете изменить свои персональные данные'
        driver.quit()

    def test_go_to_constructor_from_personal_account(self):
        """
        Провера перехода в конструктор из личной учетной записи по кнопке "Конструктор"
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
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestChangingPages.user_email)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestChangingPages.user_password)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert driver.find_element(By.XPATH, locators.CONSTRUCTOR_HEADER).text == 'Соберите бургер'
        driver.quit()

    def test_go_to_main_page_from_personal_account(self):
        """
        Провера перехода на главную из личной учетной записи по кнопке "Логотипа"
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
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_EMAIL).send_keys(TestChangingPages.user_email)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_INPUT_PASSWORD).send_keys(TestChangingPages.user_password)
        driver.find_element(By.XPATH, locators.AUTHORIZATION_BUTTON_LOGIN).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.INFORMATION_IN_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, locators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert driver.find_element(By.XPATH, locators.CONSTRUCTOR_HEADER).text == 'Соберите бургер'
        driver.quit()
