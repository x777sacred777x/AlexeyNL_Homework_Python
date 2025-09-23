# Импортируем класс By, который позволяет указывать тип локатора (CSS,
# XPATH и т.д.)
from selenium.webdriver.common.by import By

# Импортируем allure для создания отчетов
import allure


class Information:
    """Класс для работы с формой личных данных."""

    def __init__(self, driver):
        """
        Инициализация формы данных.

        Args:
            driver: WebDriver для управления браузером
        """
        # Сохраняем переданный драйвер в атрибуте объекта
        self._driver = driver

    @allure.step(
        "Заполнение формы данными: {first_name}, {last_name}, {postal_code}")
    def fill_out_the_forms(
            self,
            first_name: str,
            last_name: str,
            postal_code: str) -> None:
        """
        Заполнение формы личными данными.

        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            postal_code (str): Почтовый индекс
        """
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
