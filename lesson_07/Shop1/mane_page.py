# Импортируем класс By для указания типа локатора (CSS, XPATH и т.д.)
from selenium.webdriver.common.by import By


class MainPage:
    # Конструктор класса — принимает драйвер браузера (webdriver)
    def __init__(self, driver):
        self._driver = driver  # Сохраняем драйвер в атрибуте объекта

    # Метод для открытия страницы
    def get(self):
        # Открываем сайт
        self._driver.get("https://www.saucedemo.com/")
        # Разворачиваем окно браузера на весь экран
        self._driver.maximize_window()
        # Устанавливаем неявное ожидание (до 10 секунд на поиск элементов)
        self._driver.implicitly_wait(10)

    # Метод для авторизации на сайте
    def authorization(self, user_name, password):
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
