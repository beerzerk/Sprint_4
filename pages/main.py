from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import time


class MainPage:
    button_order_header = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    button_order_page = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    logo_yandex = [By.CSS_SELECTOR, "[alt = 'Yandex']"]
    logo_scooter = [By.CSS_SELECTOR, "[alt = 'Scooter']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу по URL")
    def open_page(self, host):
        self.driver.get(host)

    @allure.step("Получаем значение URL")
    def get_url(self, url):
        WebDriverWait(self.driver, timeout=5).until(ec.url_contains(url))
        return self.driver.current_url

    @allure.step("Прокручиваем страницу")
    def scroll_to_faq(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    @allure.step("Нажимаем кнопку Заказать в хэдере")
    def click_button_order_header(self):
        self.driver.find_element(*self.button_order_header).click()

    @allure.step("Нажимаем кнопку Заказать в разделе Как это работает")
    def click_button_order_page(self):
        self.driver.find_element(*self.button_order_page).click()

    @allure.step("Нажимаем логотип Самокат")
    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    @allure.step("Нажимаем логотип Yandex")
    def click_logo_yandex(self, tab):
        self.driver.find_element(*self.logo_yandex).click()
        window_after = self.driver.window_handles[tab]
        self.driver.switch_to.window(window_after)
