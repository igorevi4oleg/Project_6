from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_question(self, index):
        questions = self.driver.find_elements(By.CSS_SELECTOR, ".accordion__button")
        if index >= len(questions):
            raise IndexError(f"Вопрос с индексом {index} отсутствует. Доступно вопросов: {len(questions)}")
        question = questions[index]

        # Прокрутка к элементу с учетом границ viewport
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)

        # Убедимся, что элемент кликабелен
        ActionChains(self.driver).move_to_element(question).perform()

        # Ожидание кликабельности
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question)
        )
        question.click()

    def get_answer_text(self, index):
        # Получаем все ответы на вопросы
        answers = self.driver.find_elements(By.CSS_SELECTOR, ".accordion__panel")
        if index >= len(answers):
            raise IndexError(f"Ответ для вопроса с индексом {index} отсутствует. Доступно ответов: {len(answers)}")
        # Возвращаем текст ответа
        return answers[index].text

    def get_total_questions(self):
        # Возвращаем количество всех доступных вопросов
        questions = self.driver.find_elements(By.CSS_SELECTOR, ".accordion__button")
        return len(questions)

    def click_order_button(self, position="top"):
        # Находим кнопку "Заказать"
        if position == "top":
            order_button = self.driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g")
        elif position == "bottom":
            order_button = self.driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
        else:
            raise ValueError(f"Неизвестная позиция кнопки: {position}")

        # Кликаем по кнопке
        order_button.click()