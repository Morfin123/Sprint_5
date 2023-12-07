import pytest
from selenium import webdriver


@pytest.fixtur
def get_driver(request):
    """
    Инициализация вебрайвера в Chromebrowser
    :param request:
    :return:
    """
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield
    driver.quit()
