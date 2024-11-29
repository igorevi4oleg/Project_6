import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Создаем экземпляр браузера Firefox
    driver = webdriver.Firefox()
    # Открываем нужную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver  # передаем управление тесту
    # После теста закрываем браузер
    driver.quit()

# Фикстура для страницы - главный экран
@pytest.fixture
def main_page(driver):
    from page_objects.main_page import MainPage
    return MainPage(driver)

# Фикстура для страницы заказа
@pytest.fixture
def order_page(driver):
    from page_objects.order_page import OrderPage
    return OrderPage(driver)