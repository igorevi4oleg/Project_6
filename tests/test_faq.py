import pytest
from selenium import webdriver
from page_objects.main_page import MainPage

@pytest.mark.parametrize("index", range(0, 10))  # Параметризация для проверки всех доступных вопросов
def test_questions_dropdown(driver, main_page, index):
    total_questions = main_page.get_total_questions()

    # Проверяем, что индекс существует в пределах доступных вопросов
    if index < total_questions:
        main_page.open_question(index)
        answer_text = main_page.get_answer_text(index)
        assert len(answer_text) > 0, f"Ответ для вопроса с индексом {index} отсутствует"
    else:
        pytest.skip(f"Вопрос с индексом {index} не существует, пропускаем тест")


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()