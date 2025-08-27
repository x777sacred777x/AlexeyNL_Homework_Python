from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator_operations(driver):
    """
    Тестирует вычисления на калькуляторе с различными выражениями.
    Плавное равномерное выполнение теста с использованием ожиданий.
    """

    def click_button(key):
        """Кликает на кнопку калькулятора с ожиданием кликабельности"""
        xpath = f"//span[text()='{key}' and contains(@class, 'btn')]"
        button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, xpath))
        )
        button.click()

    # Ожидаем загрузку калькулятора
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'delay'))
    )

    # Установка задержки выполнения операций калькулятора на 45 секунд
    delay_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'delay'))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # Получаем элемент экрана для отслеживания изменений
    screen_element = driver.find_element(By.CSS_SELECTOR, 'div.screen')

    # Запоминаем текущий текст перед началом операции
    initial_text = screen_element.text

    # Выполнение операции: 7 + 8 =
    click_button('7')
    click_button('+')
    click_button('8')
    click_button('=')

    # Ожидаем, когда текст на экране изменится (начнется вычисление)
    WebDriverWait(driver, 10).until(lambda d: screen_element.text !=
                                    initial_text and screen_element.text != '')

    # Ожидаем конкретный результат '15' с учетом длительной задержки
    WebDriverWait(driver, 50).until(
        lambda d: screen_element.text == '15'
    )

    # Проверяем окончательный результат
    final_result = screen_element.text
    assert final_result == '15', (f"Ожидался результат '15', "
                                  f"но получен '{final_result}'")

    # Выводим результат для наглядности
    print(f"✓ Успешно выполнена операция: 7 + 8 = {final_result}")
    print("Тест завершен успешно - калькулятор работает"
          " корректно с задержкой 45 секунд")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
