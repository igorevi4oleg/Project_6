import allure
from page_objects.base_page import BasePage
from .locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, name, surname, address, phone, metro_station=None):
        self.send_keys_to_element(*OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_element(*OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys_to_element(*OrderPageLocators.ADDRESS_FIELD, address)
        self.send_keys_to_element(*OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Выбор станции метро")
    def select_metro_station(self):
        self.click_element(*OrderPageLocators.METRO_FIELD)
        self.click_element(*OrderPageLocators.METRO_FIRST_OPTION)

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.click_element(*OrderPageLocators.SUBMIT_BUTTON)

    @allure.step("Выбор даты доставки: {date}")
    def set_delivery_date(self, date):
        self.send_keys_to_element(*OrderPageLocators.DELIVERY_DATE_FIELD, date)

    @allure.step("Выбор периода аренды: {period}")
    def select_rental_period(self, period):
        self.click_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(*OrderPageLocators.RENTAL_PERIOD_OPTION(period))

    @allure.step("Подтверждение отправки заказа")
    def accept_order(self):
        self.click_element(*OrderPageLocators.ACCEPT_ORDER_BUTTON)
        self.click_element(*OrderPageLocators.CONFIRM_YES_BUTTON)
        self.click_element(*OrderPageLocators.STATUS_BUTTON)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url