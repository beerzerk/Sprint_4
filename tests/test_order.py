from selenium import webdriver
from pages.main import *
from pages.order_first_step import *
from pages.order_second_step import *
import data_for_tests
import allure
import time


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Оформление через кнопку Заказать в хэдере")
    def test_order_one(self):
        main_page = MainPage(self.driver)
        order_first_step = OrderFirstStep(self.driver)
        order_second_step = OrderSecondStep(self.driver)
        main_page.open_page("https://qa-scooter.praktikum-services.ru/")
        main_page.click_button_order_header()
        order_first_step.input_data(
            data_for_tests.test_case_1["name"],
            data_for_tests.test_case_1["surname"],
            data_for_tests.test_case_1["address"],
            data_for_tests.test_case_1["metro"],
            data_for_tests.test_case_1["phone"])
        order_first_step.click_next()
        order_second_step.input_rent(
            data_for_tests.test_case_1["when"],
            data_for_tests.test_case_1["days"],
            data_for_tests.test_case_1["color"],
            data_for_tests.test_case_1["comment"])
        order_second_step.click_button_submit()
        order_second_step.click_button_confirm()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
        order_second_step.click_button_check_status()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//button[contains(text(), 'Отменить заказ')]")

    @allure.title("Оформление через раздел Как это работает")
    def test_order_two(self):
        main_page = MainPage(self.driver)
        order_first_step = OrderFirstStep(self.driver)
        order_second_step = OrderSecondStep(self.driver)
        main_page.open_page("https://qa-scooter.praktikum-services.ru/")
        main_page.scroll_to_faq()
        main_page.click_button_order_page()
        order_first_step.input_data(
            data_for_tests.test_case_2["name"],
            data_for_tests.test_case_2["surname"],
            data_for_tests.test_case_2["address"],
            data_for_tests.test_case_2["metro"],
            data_for_tests.test_case_2["phone"])
        order_first_step.click_next()
        order_second_step.input_rent(
            data_for_tests.test_case_2["when"],
            data_for_tests.test_case_2["days"],
            data_for_tests.test_case_2["color"],
            data_for_tests.test_case_2["comment"])
        order_second_step.click_button_submit()
        order_second_step.click_button_confirm()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
        order_second_step.click_button_check_status()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//button[contains(text(), 'Отменить заказ')]")

    @allure.title("Проверка кликов по логотипам")
    def test_logo_click(self):
        main_page = MainPage(self.driver)
        main_page.open_page("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_scooter()
        assert main_page.get_url("praktikum") == "https://qa-scooter.praktikum-services.ru/"
        main_page.click_logo_yandex(1)
        assert main_page.get_url("yandex") == "https://yandex.ru"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
