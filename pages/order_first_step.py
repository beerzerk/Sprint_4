from selenium.webdriver.common.by import By
import allure


class OrderFirstStep:
    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    dropdown_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    select_metro = [By.CSS_SELECTOR, "[class='select-search__select']"]
    input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, "//button[text()='Далее']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем данные Для кого")
    def input_data(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.input_name).send_keys(name)
        self.driver.find_element(*self.input_surname).send_keys(surname)
        self.driver.find_element(*self.input_address).send_keys(address)
        self.driver.find_element(*self.dropdown_metro).send_keys(metro)
        self.driver.find_element(*self.select_metro).click()
        self.driver.find_element(*self.input_phone).send_keys(phone)

    @allure.step("Нажимаем Далее")
    def click_next(self):
        self.driver.find_element(*self.button_next).click()
