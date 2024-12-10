import pytest
import allure


@pytest.mark.usefixtures("driver")
class TestMainPage:
    @allure.title("Проверка клика по логотипу 'Самоката'")
    def test_click_scooter_logo(self, main_page):

        main_page.click_order_button()
        main_page.click_scooter_logo()  # Клик по логотипу "Самоката"

        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", \
            "Не удалось перейти на главную страницу Самоката."

    @allure.title("Проверка клика по логотипу 'Yandex'")
    def test_click_yandex_logo(self, main_page):
        main_page.click_yandex_logo()

        main_page.switch_to_new_window()

        main_page.wait_for_url_to_be("https://dzen.ru/?yredirect=true")

        assert main_page.get_current_url() == "https://dzen.ru/?yredirect=true", \
            "Не удалось открыть главную страницу Дзена."