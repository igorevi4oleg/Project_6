import pytest
import allure
from page_objects.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class TestMainPage:
    @allure.title("Проверка клика по логотипу 'Самоката'")
    def test_click_scooter_logo(self, driver, main_page):

        main_page.click_order_button()
        main_page.click_scooter_logo()  # Клик по логотипу "Самоката"
        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", "Не удалось перейти на главную страницу Самоката."

    @allure.title("Проверка клика по логотипу 'Yandex'")
    def test_click_yandex_logo(self, driver,main_page):

        main_page.click_yandex_logo()  # Клик по логотипу "Яндекса"

        # Переключаемся на новое окно
        driver.switch_to.window(driver.window_handles[1])

        # Ожидаем, что URL нового окна соответствует главной странице Дзена
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://dzen.ru/?yredirect=true")
        )

        # Проверяем, что открылся сайт Дзена
        assert driver.current_url == "https://dzen.ru/?yredirect=true", "Не удалось открыть главную страницу Дзена."