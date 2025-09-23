# Импортируем класс By для указания типа локатора (CSS, XPATH и т.д.)
from selenium.webdriver.common.by import By

# Импортируем WebDriverWait для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait

# Импортируем набор готовых условий ожидания (expected_conditions)
from selenium.webdriver.support import expected_conditions as ec

# Импортируем исключение, которое выбрасывается при превышении времени ожидания
from selenium.common.exceptions import TimeoutException

# Импортируем allure для создания отчетов
import allure


class Calc:
    """Класс для работы с медленным калькулятором."""

    def __init__(self, driver):
        """
        Инициализация калькулятора.

        Args:
            driver: WebDriver для управления браузером
        """
        self._driver = driver
        with allure.step("Открытие страницы с калькулятором"):
            self._driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            # Разворачиваем окно браузера на весь экран
            self._driver.maximize_window()

    @allure.step("Установка задержки в {tern} секунд")
    def waits_seconds(self, tern: int) -> None:
        """
        Установка задержки перед выводом результата.

        Args:
            tern (int): Задержка в секундах
        """
        # Находим поле ввода задержки по CSS-селектору
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        # Очищаем поле
        input_field.clear()
        # Вводим значение задержки
        input_field.send_keys(tern)

    @allure.step("Выполнение операции 7 + 8")
    def sum(self) -> None:
        """Выполнение операции сложения 7 + 8."""
        # Нажимаем кнопку "7"
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        # Нажимаем кнопку "+"
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        # Нажимаем кнопку "8"
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        # Нажимаем кнопку "="
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидание результата '15'")
    def wait(self) -> None:
        """Ожидание появления результата на экране."""
        try:
            # Ждём до 46 секунд, проверяя каждые 0.1 секунды,
            # пока в элементе с классом ".screen" не появится текст "15"
            WebDriverWait(
                self._driver, 46, 0.1).until(
                ec.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"), "15"))
        except TimeoutException:
            # Если время ожидания истекло — выводим сообщение
            with allure.step("Время ожидания истекло"):
                print("Время вышло")

    @allure.step("Получение результата вычислений")
    def sum_result(self) -> str:
        """
        Получение результата с экрана калькулятора.

        Returns:
            str: Текст результата
        """
        # Находим элемент с классом ".screen" и получаем его текст
        result_field = self._driver.find_element(
            By.CSS_SELECTOR, ".screen").text
        # Выводим результат в консоль
        print(result_field)
        # Возвращаем результат для дальнейшей проверки в тесте
        return result_field

    @allure.step("Закрытие браузера")
    def close_driver(self) -> None:
        """Закрытие браузера."""
        self._driver.quit()
