# Импортируем webdriver для управления браузером
from selenium import webdriver

# Импортируем ChromeService для запуска Chrome через сервисный объект
from selenium.webdriver.chrome.service import Service as ChromeService

# Импортируем менеджер драйверов, чтобы автоматически скачивать и
# подключать нужный ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем наш класс Calc, который инкапсулирует работу с "медленным
# калькулятором"
from calc import Calc

# Импортируем allure для создания отчетов
import allure

# Импортируем pytest как фреймворк для тестирования
# import pytest


@allure.feature("Медленный калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест работы медленного калькулятора с задержкой 45 секунд")
@allure.description("""
Проверка работы калькулятора с большой задержкой:
1. Установка задержки 45 секунд
2. Выполнение операции 7 + 8
3. Ожидание результата
4. Проверка что результат равен 15
""")
def test_calc():
    """Тест работы медленного калькулятора."""
    with allure.step("Запуск браузера Chrome"):
        # Создаём экземпляр браузера Chrome
        # ChromeDriverManager().install() — автоматически скачивает
        # подходящий драйвер
        # ChromeService(...) — оборачивает драйвер в сервис для корректного
        # запуска
        browser = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()))

    try:
        with allure.step("Инициализация калькулятора"):
            # Создаём объект калькулятора, передавая ему драйвер браузера
            # В конструкторе Calc сразу откроется страница
            # калькулятора и развернётся окно
            calc = Calc(browser)

        with allure.step("Установка задержки в 45 секунд"):
            # Устанавливаем задержку в 45 секунд перед показом результата
            calc.waits_seconds(45)

        with allure.step("Выполнение операции сложения 7 + 8"):
            # Выполняем операцию сложения 7 + 8
            calc.sum()

        with allure.step("Ожидание результата"):
            # Ждём, пока на экране калькулятора появится результат
            calc.wait()

        with allure.step("Проверка результата"):
            # Получаем результат с экрана калькулятора
            result_field = calc.sum_result()
            # Проверяем, что результат равен "15"
            assert result_field == "15", "Результат не равен 15"

    finally:
        with allure.step("Закрытие браузера"):
            # Закрываем браузер
            calc.close_driver()
