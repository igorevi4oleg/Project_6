from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    QUESTIONS_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    ANSWERS_TEXTS = (By.CSS_SELECTOR, ".accordion__panel")
    QUESTIONS_SECTION = (By.CSS_SELECTOR, ".accordion__item")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Адрес')]")
    PHONE_FIELD = (By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and contains(@placeholder, 'Телефон')]")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_FIRST_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]")
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTION = lambda period: (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{period}']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")