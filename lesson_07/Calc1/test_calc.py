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


def test_calc():
    # Создаём экземпляр браузера Chrome
    # ChromeDriverManager().install() — автоматически скачивает подходящий драйвер
    # ChromeService(...) — оборачивает драйвер в сервис для корректного запуска
    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()))

    # Создаём объект калькулятора, передавая ему драйвер браузера
    # В конструкторе Calc сразу откроется страница калькулятора и развернётся
    # окно
    calc = Calc(browser)

    # Устанавливаем задержку в 45 секунд перед показом результата
    calc.waits_seconds(45)

    # Выполняем операцию сложения 7 + 8
    calc.sum()

    # Ждём, пока на экране калькулятора появится результат
    calc.wait()

    # Получаем результат с экрана калькулятора
    result_field = calc.sum_resuit()

    # Проверяем, что результат равен "15"
    assert result_field == "15", "Результат не равен 15"

    # Закрываем браузер
    calc.close_driver()
