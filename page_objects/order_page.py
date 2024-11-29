from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def select_metro_station(self):
        try:
            metro_field = self.wait_for_element(By.XPATH, "//input[@placeholder='* Станция метро']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", metro_field)
            metro_field.click()
            print("Клик по полю метро выполнен.")

            metro_list = self.wait_for_element(By.XPATH, "//div[contains(@class, 'select-search')]")
            if not metro_list.is_displayed():
                raise Exception("Выпадающий список станций метро не отображается.")

            first_station = self.wait_for_element(By.XPATH, "//div[contains(@class, 'select-search__select')]")
            first_station.click()
            print("Выбрана первая станция метро.")
        except Exception as e:
            print(f"Ошибка в методе select_metro_station: {str(e)}")
            raise

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def fill_order_form(self, name, surname, address, phone, metro_station=None):
        # Используем XPath для поиска полей ввода, по их классам или другим аттрибутам
        name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Имя')]")))
        name_field.send_keys(name)

        surname_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Фамилия')]")))
        surname_field.send_keys(surname)

        address_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Адрес')]")))
        address_field.send_keys(address)

        phone_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Телефон')]")))
        phone_field.send_keys(phone)


    def submit_order(self):
        # Клик по кнопке "Далее"
        next_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Далее')]")))
        next_button.click()

    def set_delivery_date(self, date):
        # Нажать на поле даты и ввести значение
        date_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"))
        )
        date_field.click()
        date_field.clear()
        date_field.send_keys(date)

    def select_rental_period(self, period):
        # Убедимся, что календарь закрыт, кликаем вне его области
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Клик по полю выбора периода аренды
        rental_period_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Dropdown-control"))
        )
        rental_period_field.click()

        # Выбор конкретного значения из выпадающего списка
        rental_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{period}']"))
        )
        rental_option.click()

    def accept_order(self):
        # Ожидаем, пока кнопка отправки станет кликабельной
        submit_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")))
        submit_button.click()

        confirm_window = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]"))
        )

        # Ищем кнопку "Да" и нажимаем на нее
        yes_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Да')]"))
        )
        yes_button.click()

        inform_window = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]"))
        )

        status_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")))
        status_button.click()
