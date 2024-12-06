import pytest
from selenium import webdriver
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    """Создаем экземпляр браузера и открываем нужную страницу"""
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver  # Передаем управление тесту
    driver.quit()  # Закрываем браузер после теста

@pytest.fixture
def main_page(driver):
    """Фикстура для страницы главного экрана"""
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    """Фикстура для страницы оформления заказа"""
    return OrderPage(driver)