import pytest
import allure


@pytest.mark.usefixtures("driver")
class TestOrderPage:
    @allure.title("Проверка оформления заказа")
    @pytest.mark.parametrize("name, surname, address, phone, metro_station", [
        ("Иван", "Иванов", "Москва, улица Ленина", "+71234567890", None),
        ("Пётр", "Петров", "Москва, улица Пушкина", "+79876543210", None),
    ])
    def test_order_flow(self, main_page, order_page, name, surname, address, phone, metro_station):
        main_page.click_order_button()
        order_page.fill_order_form(name, surname, address, phone, metro_station)
        order_page.select_metro_station()
        order_page.submit_order()
        order_page.select_rental_period("сутки")  # Убедитесь, что метод используется
        order_page.set_delivery_date("01.12.2024")
        order_page.accept_order()
        order_page.get_current_url()

        assert order_page.get_current_url().startswith("https://qa-scooter.praktikum-services.ru/track?t=")
















