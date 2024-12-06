import allure
from page_objects.base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.step("Клик по кнопке 'Заказать' на позиции {position}")
    def click_order_button(self, position="top"):
        if position == "top":
            self.click_element(*MainPageLocators.ORDER_BUTTON_TOP)
        elif position == "bottom":
            self.click_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        else:
            raise ValueError(f"Неизвестная позиция: {position}")

    @allure.step("Прокрутка к секции вопросов")
    def scroll_to_questions_section(self):
        self.scroll_to_element(*MainPageLocators.QUESTIONS_SECTION)

    @allure.step("Ожидание кнопок вопросов")
    def wait_for_questions(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(MainPageLocators.QUESTIONS_BUTTONS)
        )

    @allure.step("Открытие вопроса с индексом {index}")
    def open_question(self, index):
        question_buttons = self.find_elements(*MainPageLocators.QUESTIONS_BUTTONS)

        if index >= len(question_buttons):
            raise IndexError(f"Вопрос с индексом {index} отсутствует. Доступно вопросов: {len(question_buttons)}")

        self.scroll_to_element(*MainPageLocators.QUESTIONS_BUTTONS)
        question_buttons[index].click()

    @allure.step("Получение текста ответа для вопроса с индексом {index}")
    def get_answer_text(self, index):
        answer_elements = self.wait.until(
            EC.presence_of_all_elements_located(MainPageLocators.ANSWERS_TEXTS)
        )
        return answer_elements[index].text

    @allure.step("Клик по логотипу 'Самоката'")
    def click_scooter_logo(self):
        self.click_element(*MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(*MainPageLocators.YANDEX_LOGO)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url