# Импортируем класс By, который позволяет указывать тип локатора (CSS,
# XPATH и т.д.)
from selenium.webdriver.common.by import By


class Information:
    # Конструктор класса — принимает драйвер браузера (webdriver)
    def __init__(self, driver):
        # Сохраняем переданный драйвер в атрибуте объекта
        self._driver = driver

    # Метод для заполнения формы с личными данными
    def fill_out_the_forms(self, first_name, last_name, postal_code):
        # Находим поле "First Name" по CSS-селектору и вводим имя
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#first-name").send_keys(first_name)

        # Находим поле "Last Name" по CSS-селектору и вводим фамилию
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#last-name").send_keys(last_name)

        # Находим поле "Postal Code" по CSS-селектору и вводим почтовый индекс
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#postal-code").send_keys(postal_code)

        # Находим кнопку "Continue" по CSS-селектору и кликаем по ней
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
