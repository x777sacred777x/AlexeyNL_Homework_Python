# Импортируем класс By для указания типа локатора (CSS, XPATH и т.д.)
from selenium.webdriver.common.by import By

# Импортируем allure для создания отчетов
import allure


class MainPage:
    """Класс для работы с главной страницей."""

    def __init__(self, driver):
        """
        Инициализация главной страницы.

        Args:
            driver: WebDriver для управления браузером
        """
        self._driver = driver  # Сохраняем драйвер в атрибуте объекта

    @allure.step("Открытие главной страницы")
    def get(self) -> None:
        """Открытие и настройка главной страницы."""
        # Открываем сайт
        self._driver.get("https://www.saucedemo.com/")
        # Разворачиваем окно браузера на весь экран
        self._driver.maximize_window()
        # Устанавливаем неявное ожидание (до 10 секунд на поиск элементов)
        self._driver.implicitly_wait(10)

    @allure.step("Авторизация пользователя {user_name}")
    def authorization(self, user_name: str, password: str) -> None:
        """
        Авторизация на сайте.

        Args:
            user_name (str): Имя пользователя
            password (str): Пароль
        """
        # Находим поле ввода логина по CSS-селектору и вводим имя пользователя
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#user-name").send_keys(user_name)
        # Находим поле ввода пароля по CSS-селектору и вводим пароль
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#password").send_keys(password)
        # Находим кнопку входа по CSS-селектору и кликаем по ней
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
