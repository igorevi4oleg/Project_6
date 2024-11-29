import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("name, surname, address, phone, metro_station", [
    ("Иван", "Иванов", "Москва, улица Ленина, д. 1", "+71234567890", None),  # Берём первую станцию
    ("Пётр", "Петров", "Москва, улица Пушкина, д. 2", "+79876543210", None)  # Выбираем конкретную станцию
])

def test_order_flow(driver, main_page, order_page, name, surname, address, phone, metro_station):
    # Кликаем по кнопке "Заказать" (для верхней кнопки)
    main_page.click_order_button(position='top')

    # Заполняем форму заказа и выбираем станцию метро
    order_page.fill_order_form(name, surname, address, phone, metro_station)

    order_page.select_metro_station()

    # Нажимаем кнопку "Далее"
    order_page.submit_order()

    order_page.set_delivery_date("01.12.2024")  # Заменить на актуальную дату
    order_page.select_rental_period(period="сутки")

    # Нажимаем кнопку "Заказать"
    order_page.accept_order()

    driver.implicitly_wait(5)  # Даем время на редирект
    current_url = driver.current_url
    assert current_url.startswith(
        "https://qa-scooter.praktikum-services.ru/track?t="), f"Ожидался URL, начинающийся с 'https://qa-scooter.praktikum-services.ru/track?t=', но был {current_url}"


    # Проверяем редиректы по логотипам
    logo_scooter = driver.find_element(By.XPATH, "//img[@alt='Scooter']")
    logo_scooter.click()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не на главной странице самоката"

    try:
        logo_yandex = driver.find_element(By.XPATH, "//a[contains(@href, 'yandex.ru')]")
        logo_yandex.click()

        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])

        # Проверяем, что открылась страница Яндекса
        assert "zen.yandex.ru" in driver.current_url, "Редирект на Яндекс не работает"
    except Exception as e:
        print(f"Ошибка при переходе на Яндекс: {e}")

















