from selenium.webdriver.common.by import By
import allure


base_url = "https://qa-scooter.praktikum-services.ru/"


class QuestionsSection:
    questions = {1: [By.ID, "accordion__heading-0"],
                 2: [By.ID, "accordion__heading-1"],
                 3: [By.ID, "accordion__heading-2"],
                 4: [By.ID, "accordion__heading-3"],
                 5: [By.ID, "accordion__heading-4"],
                 6: [By.ID, "accordion__heading-5"],
                 7: [By.ID, "accordion__heading-6"],
                 8: [By.ID, "accordion__heading-7"]}

    answers = {1: [By.ID, "accordion__panel-0"],
               2: [By.ID, "accordion__panel-1"],
               3: [By.ID, "accordion__panel-2"],
               4: [By.ID, "accordion__panel-3"],
               5: [By.ID, "accordion__panel-4"],
               6: [By.ID, "accordion__panel-5"],
               7: [By.ID, "accordion__panel-6"],
               8: [By.ID, "accordion__panel-7"]}

    def __init__(self, driver):
        self.question = None
        self.answer = None
        self.driver = driver

    @allure.step("Открываем главную страницу")
    def get_page(self):
        return self.driver.get(base_url)

    @allure.step("Прокручиваем к вопросам")
    def scroll_to_question(self, question):
        self.question = self.questions[question]
        element = self.driver.find_element(*self.question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Берем вопрос для сравнения")
    def get_question(self, question):
        self.question = self.questions[question]
        return self.driver.find_element(*self.question).text

    @allure.step("Клик на вопрос для открытия")
    def open_answer(self, question):
        self.question = self.questions[question]
        self.driver.find_element(*self.question).click()

    @allure.step("Берем ответ для сравнения")
    def get_answer(self, answer):
        self.answer = self.answers[answer]
        return self.driver.find_element(*self.answer).text
