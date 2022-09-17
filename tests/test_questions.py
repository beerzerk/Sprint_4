from selenium import webdriver
from pages.questions import QuestionsSection
import allure
from data_for_tests import questions, answers


class TestQuestionsAndAnswers:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверяем Вопрос и Ответ №1")
    def test_question_1(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(1)
        question_text = question.get_question(1)
        assert question_text == questions[1], "Текст не совпадает!"
        question.open_answer(1)
        question_answer = question.get_answer(1)
        assert question_answer == answers[1], "Текст не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №2")
    def test_question_2(self):

        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(2)
        question_text = question.get_question(2)
        assert question_text == questions[2], "Текст вопроса не совпадает!"
        question.open_answer(2)
        question_answer = question.get_answer(2)
        assert question_answer == answers[2], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №3")
    def test_question_3(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(3)
        question_text = question.get_question(3)
        assert question_text == questions[3], "Текст вопроса не совпадает!"
        question.open_answer(3)
        question_answer = question.get_answer(3)
        assert question_answer == answers[3], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №4")
    def test_question_4(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(4)
        question_text = question.get_question(4)
        assert question_text == questions[4], "Текст вопроса не совпадает!"
        question.open_answer(4)
        question_answer = question.get_answer(4)
        assert question_answer == answers[4], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №5")
    def test_question_5(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(5)
        question_text = question.get_question(5)
        assert question_text == questions[5], "Текст вопроса не совпадает!"
        question.open_answer(5)
        question_answer = question.get_answer(5)
        assert question_answer == answers[5], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №6")
    def test_question_6(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(6)
        question_text = question.get_question(6)
        assert question_text == questions[6], "Текст вопроса не совпадает!"
        question.open_answer(6)
        question_answer = question.get_answer(6)
        assert question_answer == answers[6], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №7")
    def test_question_7(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(7)
        question_text = question.get_question(7)
        assert question_text == questions[7], "Текст вопроса не совпадает!"
        question.open_answer(7)
        question_answer = question.get_answer(7)
        assert question_answer == answers[7], "Текст ответа не совпадает!"

    @allure.title("Проверяем Вопрос и Ответ №8")
    def test_question_8(self):
        question = QuestionsSection(self.driver)
        question.get_page()
        question.scroll_to_question(8)
        question_text = question.get_question(8)
        assert question_text == questions[8], "Текст вопроса не совпадает!"
        question.open_answer(8)
        question_answer = question.get_answer(8)
        assert question_answer == answers[8], "Текст ответа не совпадает!"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
