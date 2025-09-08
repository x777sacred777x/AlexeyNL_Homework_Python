# Импортируем класс By для указания типа локатора (CSS, XPATH и т.д.)
from selenium.webdriver.common.by import By

# Импортируем WebDriverWait для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем набор готовых условий ожидания (expected_conditions)
from selenium.webdriver.support import expected_conditions as ec

# Импортируем исключение, которое выбрасывается при превышении времени ожидания
from selenium.common.exceptions import TimeoutException


class Calc:
    # Конструктор класса — принимает драйвер браузера
    def __init__(self, driver):
        self._driver = driver
        # Открываем страницу с "медленным калькулятором"
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Разворачиваем окно браузера на весь экран
        self._driver.maximize_window()

    # Метод для установки задержки (в секундах) перед выводом результата
    # калькулятора
    def waits_seconds(self, tern):
        # Находим поле ввода задержки по CSS-селектору
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        # Очищаем поле
        input_field.clear()
        # Вводим значение задержки
        input_field.send_keys(tern)

    # Метод для выполнения операции сложения 7 + 8
    def sum(self):
        # Нажимаем кнопку "7"
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        # Нажимаем кнопку "+"
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        # Нажимаем кнопку "8"
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        # Нажимаем кнопку "="
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Метод для ожидания появления результата "15" на экране калькулятора
    def wait(self):
        try:
            # Ждём до 46 секунд, проверяя каждые 0.1 секунды,
            # пока в элементе с классом ".screen" не появится текст "15"
            WebDriverWait(
                self._driver, 46, 0.1).until(
                ec.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"), "15"))
        except TimeoutException:
            # Если время ожидания истекло — выводим сообщение
            print("Время вышло")

    # Метод для получения и возврата результата с экрана калькулятора
    def sum_resuit(self):
        # Находим элемент с классом ".screen" и получаем его текст
        result_field = self._driver.find_element(
            By.CSS_SELECTOR, ".screen").text
        # Выводим результат в консоль
        print(result_field)
        # Возвращаем результат для дальнейшей проверки в тесте
        return result_field

    # Метод для закрытия браузера
    def close_driver(self):
        self._driver.quit()
