import pytest
import allure


@pytest.mark.parametrize("index", range(0, 8))
@allure.title("Проверка выпадающих вопросов")
def test_question_and_answer(main_page, index):
    main_page.wait_for_questions()

    main_page.scroll_to_questions_section()

    main_page.open_question(index)

    answer_text = main_page.get_answer_text(index)
    assert len(answer_text) > 0, f"Ответ для вопроса с индексом {index} отсутствует"