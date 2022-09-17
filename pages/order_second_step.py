from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class OrderSecondStep:
    input_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    dropdown_rental_period = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    rental_periods = [By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)"]
    rental_period = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    colors = {
        "black": [By.ID, "black"],
        "grey": [By.ID, "grey"]
    }
    input_comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    button_submit = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    button_confirm = [By.XPATH, "//button[text()='Да']"]
    button_check_status = [By.XPATH, "//button[text()='Посмотреть статус']"]
    button_cancel = [By.XPATH, "//button[text()='Отменить заказ']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем данные Про аренду")
    def input_rent(self, when, days, color, comment):
        self.driver.find_element(*self.input_date).send_keys(when)
        self.driver.find_element(*self.input_date).send_keys(Keys.ENTER)
        self.driver.find_element(*self.dropdown_rental_period).click()
        self.driver.find_element(*self.rental_period[days]).click()
        self.driver.find_element(*self.colors[color]).click()
        self.driver.find_element(*self.input_comment).send_keys(comment)

    @allure.step("Нажимаем кнопку Заказать")
    def click_button_submit(self):
        self.driver.find_element(*self.button_submit).click()

    @allure.step("Нажимаем кнопку Да для подтверждения заказа")
    def click_button_confirm(self):
        self.driver.find_element(*self.button_confirm).click()

    @allure.step("Нажимаем кнопку Посмотреть статус")
    def click_button_check_status(self):
        self.driver.find_element(*self.button_check_status).click()
